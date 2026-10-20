from datetime import datetime, timezone
from threading import Lock

from .validation import validate_case
from .agents.analista import analisar
from .agents.especialista import avaliar
from .agents.planejador import planejar


HISTORY = []
_HISTORY_LOCK = Lock()


def _registrar_historico(entry):
    """Registra uma execução no histórico em memória."""
    with _HISTORY_LOCK:
        HISTORY.append(entry)


def _resposta_erro(caso_id, codigo, mensagem, pendencias=None):
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


def run_case(caso_id, dados_caso, historico_id=None):
    """
    Executa o fluxo do CardioIA:

    1. Validação da entrada.
    2. Analista de Risco.
    3. Especialista em Protocolos.
    4. Planejador de Resposta.
    5. Registro do histórico.

    Os resultados de cada etapa são preservados em memória.
    """

    entry = {
        "caso_id": caso_id,
        "historico_id": historico_id or caso_id,
        "inicio_utc": datetime.now(timezone.utc).isoformat(),
        "etapas": [],
        "resultados_preservados": {},
        "estado_final": "em_execucao",
        "erro": None,
    }

    try:
        # 1. Validar os dados de entrada.
        issues = validate_case(dados_caso)

        if issues:
            resposta = _resposta_erro(
                caso_id,
                "ENTRADA_INVALIDA",
                "; ".join(issues),
            )

            entry["estado_final"] = "erro"
            entry["erro"] = resposta["erro"]
            return resposta

        entry["etapas"].append("Validacao de Entrada")

        # 2. Analista de Risco.
        analise = analisar(caso_id, dados_caso)

        entry["etapas"].append("Analista de Risco")
        entry["resultados_preservados"]["analise"] = analise

        if not isinstance(analise, dict):
            resposta = _resposta_erro(
                caso_id,
                "RESPOSTA_INVALIDA",
                "O Analista de Risco não retornou um objeto válido.",
            )

            entry["estado_final"] = "erro"
            entry["erro"] = resposta["erro"]
            return resposta

        if analise.get("status") == "erro":
            entry["estado_final"] = "erro"
            entry["erro"] = analise.get("erro")
            return analise

        # 3. Especialista em Protocolos.
        protocolos = avaliar(caso_id, dados_caso)

        entry["etapas"].append("Especialista em Protocolos")
        entry["resultados_preservados"]["protocolos"] = protocolos

        if not isinstance(protocolos, dict):
            resposta = _resposta_erro(
                caso_id,
                "RESPOSTA_INVALIDA",
                "O Especialista em Protocolos não retornou um objeto válido.",
            )

            entry["estado_final"] = "erro"
            entry["erro"] = resposta["erro"]
            return resposta

        if protocolos.get("status") == "erro":
            entry["estado_final"] = "erro"
            entry["erro"] = protocolos.get("erro")
            return protocolos

        # 4. Planejador de Resposta.
        plano = planejar(caso_id, analise, protocolos)

        entry["etapas"].append("Planejador de Resposta")
        entry["resultados_preservados"]["plano"] = plano

        if not isinstance(plano, dict):
            resposta = _resposta_erro(
                caso_id,
                "RESPOSTA_INVALIDA",
                "O Planejador de Resposta não retornou um objeto válido.",
            )

            entry["estado_final"] = "erro"
            entry["erro"] = resposta["erro"]
            return resposta

        if plano.get("status") == "erro":
            entry["estado_final"] = "erro"
            entry["erro"] = plano.get("erro")
            return plano

        # 5. Consolidar as pendências de todas as etapas.
        pendencias = (
            list(analise.get("pendencias", []))
            + list(protocolos.get("pendencias", []))
            + list(plano.get("pendencias", []))
        )

        # Evitar duplicações simples no relatório.
        pendencias_unicas = []
        for pendencia in pendencias:
            if pendencia not in pendencias_unicas:
                pendencias_unicas.append(pendencia)

        status_etapas = [
            analise.get("status"),
            protocolos.get("status"),
            plano.get("status"),
        ]

        if "parcial" in status_etapas or pendencias_unicas:
            status_final = "parcial"
        else:
            status_final = "sucesso"

        resposta = {
            "versao_contrato": "1.0",
            "agente": "Orquestrador",
            "status": status_final,
            "caso_id": caso_id,
            "resultado": plano.get("resultado", {}),
            "pendencias": pendencias_unicas,
            "erro": None,
        }

        entry["estado_final"] = status_final
        return resposta

    except Exception as erro:
        resposta = _resposta_erro(
            caso_id,
            "FALHA_ORQUESTRACAO",
            f"Falha durante a execução do fluxo: {str(erro)}",
        )

        entry["estado_final"] = "erro"
        entry["erro"] = resposta["erro"]
        return resposta

    finally:
        entry["fim_utc"] = datetime.now(timezone.utc).isoformat()
        _registrar_historico(entry)


def history():
    """Retorna uma cópia do histórico de execuções."""
    with _HISTORY_LOCK:
        return [dict(item) for item in HISTORY]