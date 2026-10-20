import joblib
import pandas as pd

from .config import FEATURES, MODEL_PATH
from .validation import validate_case
from .contracts import Envelope


RULES = [
    (
        "spo2_baixa",
        "spo2_media < 88",
        "spo2_media",
        lambda d: d["spo2_media"] < 88,
        "iniciar suporte respiratório imediato",
    ),
    (
        "carga_alta",
        "carga_sistema > 85",
        "carga_sistema",
        lambda d: d["carga_sistema"] > 85,
        "abrir unidades temporárias",
    ),
    (
        "fc_alta",
        "fc_media > 120",
        "fc_media",
        lambda d: d["fc_media"] > 120,
        "iniciar monitoramento intensivo",
    ),
    (
        "eventos_altos",
        "eventos_24h > 5",
        "eventos_24h",
        lambda d: d["eventos_24h"] > 5,
        "ativar equipe de resposta rápida",
    ),
    (
        "recursos_baixos",
        "disponibilidade_recursos < 30",
        "disponibilidade_recursos",
        lambda d: d["disponibilidade_recursos"] < 30,
        "redistribuir insumos",
    ),
    (
        "espera_alta",
        "tempo_espera > 90",
        "tempo_espera",
        lambda d: d["tempo_espera"] > 90,
        "priorizar triagem emergencial",
    ),
    (
        "temperatura_alta",
        "temperatura > 38",
        "temperatura",
        lambda d: d["temperatura"] > 38,
        "iniciar protocolo infeccioso",
    ),
    (
        "densidade_alta",
        "densidade_eventos > 6",
        "densidade_eventos",
        lambda d: d["densidade_eventos"] > 6,
        "ativar plano de contingência",
    ),
    (
        "pressao_baixa",
        "pa_sistolica < 90",
        "pa_sistolica",
        lambda d: d["pa_sistolica"] < 90,
        "iniciar protocolo de choque",
    ),
]


def prever_risco(caso_id, dados_caso):
    """
    Valida os dados de entrada e utiliza o Random Forest
    treinado para prever a classe pico_risco.
    """

    issues = validate_case(dados_caso)

    if issues:
        return Envelope(
            agente="prever_risco",
            status="erro",
            caso_id=caso_id,
            erro={
                "codigo": "ENTRADA_INVALIDA",
                "mensagem": "; ".join(issues),
                "agente_origem": "prever_risco",
            },
        ).model_dump()

    if not MODEL_PATH.exists():
        return Envelope(
            agente="prever_risco",
            status="erro",
            caso_id=caso_id,
            erro={
                "codigo": "MODELO_AUSENTE",
                "mensagem": (
                    "Execute python -m src.train_model "
                    "antes de realizar a inferência."
                ),
                "agente_origem": "prever_risco",
            },
        ).model_dump()

    try:
        bundle = joblib.load(MODEL_PATH)

        if bundle["features"] != FEATURES:
            raise ValueError(
                "As features do modelo são incompatíveis "
                "com as features atuais."
            )

        modelo = bundle["model"]

        # Mantém os nomes e a ordem das features usados no treinamento.
        entrada = pd.DataFrame(
            [[dados_caso[feature] for feature in FEATURES]],
            columns=FEATURES,
        )

        probabilidades = modelo.predict_proba(entrada)[0]

        classes = list(modelo.classes_)

        if 1 not in classes:
            raise ValueError(
                "O modelo treinado não possui a classe 1."
            )

        indice_positivo = classes.index(1)

        score_risco = float(
            probabilidades[indice_positivo]
        )

        classe_prevista = int(
            modelo.predict(entrada)[0]
        )

        return {
            "versao_contrato": "1.0",
            "agente": "Analista de Risco",
            "status": "sucesso",
            "caso_id": caso_id,
            "resultado": {
                "score_risco": score_risco,
                "classe_prevista_pico_risco": classe_prevista,
                "modelo": "RandomForestClassifier",
                "observacao": (
                    "O score do modelo não é uma "
                    "probabilidade clínica calibrada."
                ),
            },
            "pendencias": [],
            "erro": None,
        }

    except Exception as erro:
        return Envelope(
            agente="prever_risco",
            status="erro",
            caso_id=caso_id,
            erro={
                "codigo": "INFERENCIA_FALHOU",
                "mensagem": str(erro),
                "agente_origem": "prever_risco",
            },
        ).model_dump()


def consultar_protocolos(caso_id, dados_caso):
    """
    Verifica as regras de protocolo definidas no enunciado
    e retorna as ações correspondentes às condições atendidas.
    """

    issues = validate_case(dados_caso)

    if issues:
        return Envelope(
            agente="consultar_protocolos",
            status="erro",
            caso_id=caso_id,
            erro={
                "codigo": "ENTRADA_INVALIDA",
                "mensagem": "; ".join(issues),
                "agente_origem": "consultar_protocolos",
            },
        ).model_dump()

    protocolos_acionados = []

    for protocolo_id, condicao, campo, regra, acao in RULES:
        if regra(dados_caso):
            protocolos_acionados.append(
                {
                    "id": protocolo_id,
                    "condicao": condicao,
                    "valor_observado": dados_caso[campo],
                    "acao": acao,
                }
            )

    # O enunciado não informa o limiar para risco sistêmico alto.
    # Portanto, não inventamos um valor para essa regra.
    pendencias = [
        {
            "regra": "risco sistêmico alto",
            "motivo": (
                "O limiar não foi informado no enunciado; "
                "a regra permanece pendente."
            ),
        }
    ]

    return {
        "versao_contrato": "1.0",
        "agente": "Especialista em Protocolos",
        "status": "parcial",
        "caso_id": caso_id,
        "resultado": {
            "protocolos_acionados": protocolos_acionados,
            "regras_pendentes": pendencias,
        },
        "pendencias": pendencias,
        "erro": None,
    }

# ============================================================
# OPENAI AGENTS SDK — FERRAMENTAS
# ============================================================

import json

from agents import function_tool


@function_tool
def ferramenta_prever_risco(
    caso_id: str,
    dados_json: str,
) -> str:
    """
    Executa a previsão de risco usando o modelo Random Forest.

    Args:
        caso_id: Identificador do caso analisado.
        dados_json: Dados do caso serializados como uma string JSON.
    """
    try:
        dados_caso = json.loads(dados_json)

        resultado = prever_risco(
            caso_id=caso_id,
            dados_caso=dados_caso,
        )

        return json.dumps(
            resultado,
            ensure_ascii=False,
            allow_nan=False,
        )

    except Exception as erro:
        return json.dumps(
            {
                "versao_contrato": "1.0",
                "agente": "Analista de Risco",
                "status": "erro",
                "caso_id": caso_id,
                "resultado": {},
                "pendencias": [],
                "erro": {
                    "codigo": "FERRAMENTA_FALHOU",
                    "mensagem": str(erro),
                    "agente_origem": "ferramenta_prever_risco",
                },
            },
            ensure_ascii=False,
        )


@function_tool
def ferramenta_consultar_protocolos(
    caso_id: str,
    dados_json: str,
) -> str:
    """
    Consulta os protocolos definidos no enunciado.

    Args:
        caso_id: Identificador do caso analisado.
        dados_json: Dados do caso serializados como uma string JSON.
    """
    try:
        dados_caso = json.loads(dados_json)

        resultado = consultar_protocolos(
            caso_id=caso_id,
            dados_caso=dados_caso,
        )

        return json.dumps(
            resultado,
            ensure_ascii=False,
            allow_nan=False,
        )

    except Exception as erro:
        return json.dumps(
            {
                "versao_contrato": "1.0",
                "agente": "Especialista em Protocolos",
                "status": "erro",
                "caso_id": caso_id,
                "resultado": {},
                "pendencias": [],
                "erro": {
                    "codigo": "FERRAMENTA_FALHOU",
                    "mensagem": str(erro),
                    "agente_origem": "ferramenta_consultar_protocolos",
                },
            },
            ensure_ascii=False,
        )