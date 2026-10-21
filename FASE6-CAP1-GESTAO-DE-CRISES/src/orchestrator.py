import json
from copy import deepcopy
from datetime import datetime, timezone
from threading import Lock
from typing import Any

from agents import Agent, Runner

from .validation import validate_case
from .tools import consultar_protocolos
from .agents.analista import analista_risco
from .agents.especialista import especialista_protocolos


HISTORY: list[dict[str, Any]] = []
_HISTORY_LOCK = Lock()


# Agente de entrada: coordena o fluxo por meio de handoffs.
orquestrador_agente = Agent(
    name="Orquestrador",
    instructions=(
        "Você é o Orquestrador do CardioIA. "
        "Sua função é coordenar o processamento do caso. "
        "Encaminhe o caso recebido imediatamente ao Analista de Risco "
        "utilizando o handoff disponível. "
        "Não invente resultados, probabilidades ou protocolos. "
        "O sistema utiliza dados sintéticos e não deve ser empregado "
        "para decisões clínicas reais."
    ),
    handoffs=[analista_risco],
)


def _registrar_historico(entrada: dict[str, Any]) -> None:
    """Registra uma execução no histórico em memória."""
    with _HISTORY_LOCK:
        HISTORY.append(deepcopy(entrada))


def _resposta_erro(
    caso_id: str,
    codigo: str,
    mensagem: str,
    pendencias: list | None = None,
) -> dict[str, Any]:
    """Cria uma resposta de erro conforme o contrato JSON v1.0."""
    return {
        "versao_contrato": "1.0",
        "agente": "Orquestrador",
        "status": "erro",
        "caso_id": caso_id,
        "resultado": {},
        "pendencias": pendencias or [],
        "erro": {
            "codigo": codigo,
            "mensagem": mensagem,
            "agente_origem": "Orquestrador",
        },
    }


def _extrair_resultados(
    execucao: Any,
) -> tuple[dict | None, dict | None]:
    """
    Extrai os resultados JSON produzidos pelas ferramentas dos agentes.
    Não utiliza o texto gerado pelo modelo como fonte dos valores calculados.
    """
    analise = None
    protocolos = None

    for item in getattr(execucao, "new_items", []):
        if "ToolCallOutputItem" not in type(item).__name__:
            continue

        saida = getattr(item, "output", None)

        if isinstance(saida, str):
            try:
                saida = json.loads(saida)
            except json.JSONDecodeError:
                continue

        if not isinstance(saida, dict):
            continue

        resultado = saida.get("resultado", {})

        if not isinstance(resultado, dict):
            continue

        if (
            "score_risco" in resultado
            and "classe_prevista_pico_risco" in resultado
        ):
            analise = saida

        elif "protocolos_acionados" in resultado:
            protocolos = saida

    return analise, protocolos


def _protocolos_validos(protocolos: Any) -> bool:
    """Verifica se existe uma resposta estruturada de protocolos."""
    return (
        isinstance(protocolos, dict)
        and isinstance(protocolos.get("resultado"), dict)
        and isinstance(
            protocolos["resultado"].get("protocolos_acionados"),
            list,
        )
        and protocolos.get("status") in ("sucesso", "parcial")
    )


def run_case(
    caso_id: str,
    dados_caso: dict,
    historico_id: str | None = None,
) -> dict[str, Any]:
    """
    Executa o fluxo:
    Orquestrador -> Analista de Risco -> Especialista em Protocolos
    -> Planejador de Resposta.

    O SDK gerencia as ferramentas e os handoffs configurados nos agentes.
    """
    entrada_historico = {
        "caso_id": caso_id,
        "historico_id": historico_id or caso_id,
        "inicio_utc": datetime.now(timezone.utc).isoformat(),
        "fim_utc": None,
        "etapas": ["Validacao de Entrada"],
        "mensagens": [],
        "itens_execucao": [],
        "estado_final": "em_execucao",
        "erro": None,
    }

    try:
        # 1. Validar a entrada antes de chamar qualquer agente.
        problemas = validate_case(dados_caso)

        if problemas:
            resposta = _resposta_erro(
                caso_id,
                "ENTRADA_INVALIDA",
                "; ".join(problemas),
            )
            entrada_historico["estado_final"] = "erro"
            entrada_historico["erro"] = resposta["erro"]
            return resposta

        pedido = {
            "caso_id": caso_id,
            "dados_caso": dados_caso,
            "instrucao": (
                "Processe o caso por meio do fluxo de agentes configurado. "
                "Preserve os valores retornados pelas ferramentas. "
                "Não invente probabilidades nem protocolos."
            ),
        }

        # 2. Iniciar o fluxo pelo Orquestrador.
        execucao = Runner.run_sync(
            orquestrador_agente,
            input=json.dumps(
                pedido,
                ensure_ascii=False,
                allow_nan=False,
            ),
            max_turns=12,
        )

        entrada_historico["mensagens"] = execucao.to_input_list()
        entrada_historico["ultimo_agente"] = getattr(
            getattr(execucao, "last_agent", None),
            "name",
            None,
        )

        entrada_historico["itens_execucao"] = [
            type(item).__name__
            for item in getattr(execucao, "new_items", [])
        ]

        # 3. Extrair os valores estruturados das ferramentas.
        analise, protocolos = _extrair_resultados(execucao)

        # 4. Se o fluxo inicial não retornou protocolos estruturados,
        # tentar executar o Especialista pelo SDK antes do fallback.
        if not _protocolos_validos(protocolos):
            pedido_especialista = json.dumps(
                {
                    "caso_id": caso_id,
                    "dados_caso": dados_caso,
                    "instrucao": (
                        "Consulte obrigatoriamente a ferramenta "
                        "ferramenta_consultar_protocolos com o caso "
                        "e os dados fornecidos. "
                        "Preserve a saída estruturada da ferramenta. "
                        "Depois, transfira o controle ao Planejador "
                        "de Resposta pelo handoff disponível."
                    ),
                },
                ensure_ascii=False,
                allow_nan=False,
            )

            execucao_especialista = Runner.run_sync(
                especialista_protocolos,
                input=pedido_especialista,
                max_turns=8,
            )

            # Extrair a saída da segunda execução.
            _, protocolos_especialista = _extrair_resultados(
                execucao_especialista
            )

            entrada_historico["mensagens"].extend(
                execucao_especialista.to_input_list()
            )
            entrada_historico["itens_execucao"].extend(
                type(item).__name__
                for item in execucao_especialista.new_items
            )

            entrada_historico["ultimo_agente"] = getattr(
                getattr(execucao_especialista, "last_agent", None),
                "name",
                None,
            )

            if _protocolos_validos(protocolos_especialista):
                protocolos = protocolos_especialista

            # Guardar a síntese mais recente para a resposta.
            execucao = execucao_especialista

        # 5. Usar as regras determinísticas apenas se as tentativas
        # pelo SDK não produzirem uma saída estruturada válida.
        if not _protocolos_validos(protocolos):
            protocolos = consultar_protocolos(
                caso_id=caso_id,
                dados_caso=dados_caso,
            )
            entrada_historico["fallback_protocolos"] = True

        # 6. Verificar o resultado do Analista.
        if analise is None:
            pendencias = [
                {
                    "etapa": "Analista de Risco",
                    "motivo": (
                        "Não foi possível identificar a saída estruturada "
                        "da ferramenta de previsão."
                    ),
                }
            ]

        elif analise.get("status") == "erro":
            resposta = analise
            entrada_historico["estado_final"] = "erro"
            entrada_historico["erro"] = resposta.get("erro")
            return resposta

        else:
            pendencias = []
            entrada_historico["etapas"].append("Analista de Risco")

        # 7. Verificar o resultado do Especialista.
        if protocolos is None:
            pendencias.append(
                {
                    "etapa": "Especialista em Protocolos",
                    "motivo": (
                        "Não foi possível obter uma saída estruturada "
                        "da ferramenta de protocolos."
                    ),
                }
            )

        elif protocolos.get("status") == "erro":
            resposta = protocolos
            entrada_historico["estado_final"] = "erro"
            entrada_historico["erro"] = resposta.get("erro")
            return resposta

        else:
            entrada_historico["etapas"].append(
                "Especialista em Protocolos"
            )

        # 8. Consolidar os valores calculados e os protocolos.
        risco = (
            analise.get("resultado", {})
            if analise is not None
            else {}
        )

        resultado_protocolos = (
            protocolos.get("resultado", {})
            if protocolos is not None
            else {}
        )

        protocolos_sugeridos = resultado_protocolos.get(
            "protocolos_acionados",
            [],
        )

        score = risco.get("score_risco")
        classe = risco.get("classe_prevista_pico_risco")

        if classe == 1:
            classificacao = "Pico de risco previsto"
        elif classe == 0:
            classificacao = "Sem pico de risco previsto"
        else:
            classificacao = None

        # Propagar pendências identificadas pelas ferramentas.
        pendencias_protocolos = (
            protocolos.get("pendencias", [])
            if protocolos is not None
            else []
        )
        pendencias.extend(pendencias_protocolos)

        # Remover duplicações idênticas.
        pendencias_unicas = []
        for pendencia in pendencias:
            if pendencia not in pendencias_unicas:
                pendencias_unicas.append(pendencia)

        saida_final = getattr(execucao, "final_output", None)
        if not isinstance(saida_final, str):
            saida_final = (
                str(saida_final)
                if saida_final is not None
                else ""
            )

        # 9. Formar a resposta padronizada.
        resposta = {
            "versao_contrato": "1.0",
            "agente": "Orquestrador",
            "status": (
                "parcial"
                if pendencias_unicas
                else "sucesso"
            ),
            "caso_id": caso_id,
            "resultado": {
                "resultado_risco": risco,
                "probabilidade_estimada_modelo": score,
                "classe_prevista_pico_risco": classe,
                "classificacao_risco": classificacao,
                "protocolos_sugeridos": protocolos_sugeridos,
                "plano_resposta": {
                    "protocolos_recomendados": protocolos_sugeridos,
                    "resumo": (
                        f"Caso {caso_id}: "
                        f"{len(protocolos_sugeridos)} protocolo(s) "
                        "identificado(s)."
                    ),
                    "limitacoes": [
                        "Os dados utilizados são sintéticos.",
                        (
                            "O score do modelo não é uma probabilidade "
                            "clínica calibrada."
                        ),
                        (
                            "O limiar de risco sistêmico alto não foi "
                            "especificado no enunciado."
                        ),
                    ],
                    "sintese_planejador": saida_final,
                },
            },
            "pendencias": pendencias_unicas,
            "erro": None,
        }

        entrada_historico["estado_final"] = resposta["status"]

        if (
            "Planejador de Resposta"
            not in entrada_historico["etapas"]
        ):
            entrada_historico["etapas"].append(
                "Planejador de Resposta"
            )

        return resposta

    except Exception as erro:
        resposta = _resposta_erro(
            caso_id,
            "FALHA_ORQUESTRACAO",
            f"Falha durante a execução do fluxo: {erro}",
        )

        entrada_historico["estado_final"] = "erro"
        entrada_historico["erro"] = resposta["erro"]
        return resposta

    finally:
        entrada_historico["fim_utc"] = datetime.now(
            timezone.utc
        ).isoformat()

        _registrar_historico(entrada_historico)


def history() -> list[dict[str, Any]]:
    """Retorna uma cópia do histórico de execuções."""
    with _HISTORY_LOCK:
        return deepcopy(HISTORY)