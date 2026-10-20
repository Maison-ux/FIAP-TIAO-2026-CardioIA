from agents import Agent


planejador_resposta = Agent(
    name="Planejador de Resposta",
    instructions="""
Você é o Planejador de Resposta do CardioIA.

Sua função é consolidar os resultados do Analista de Risco
e do Especialista em Protocolos.

Regras:
1. Preserve os resultados e as pendências recebidos.
2. Não invente previsões, protocolos ou limiares.
3. Não interprete o score como probabilidade clínica calibrada.
4. Informe que os dados utilizados são sintéticos.
5. O limiar de risco sistêmico alto não foi especificado.
6. Não apresente o plano como orientação clínica real.
""",
)


def planejar(caso_id: str, analise: dict, protocolos: dict) -> dict:
    """Consolida os resultados dos dois agentes anteriores."""

    pendencias = (
        list(analise.get("pendencias", []))
        + list(protocolos.get("pendencias", []))
    )

    resultado_risco = analise.get("resultado", {})
    resultado_protocolos = protocolos.get("resultado", {})

    protocolos_acionados = resultado_protocolos.get(
        "protocolos_acionados", []
    )

    limitacoes = [
        "Dados sintéticos; não utilizar para decisões clínicas reais.",
        "O score não é uma probabilidade clínica calibrada.",
        "O limiar de risco sistêmico alto não foi especificado.",
    ]

    return {
        "versao_contrato": "1.0",
        "agente": "Planejador de Resposta",
        "status": "parcial" if pendencias else "sucesso",
        "caso_id": caso_id,
        "resultado": {
            "resultado_risco": resultado_risco,
            "plano_resposta": {
                "protocolos_recomendados": protocolos_acionados,
                "justificativas": [
                    "Os protocolos são baseados nas regras explícitas "
                    "definidas no enunciado."
                ],
                "limitacoes": limitacoes,
                "resumo": (
                    f"Caso {caso_id}: "
                    f"{len(protocolos_acionados)} protocolo(s) identificado(s)."
                ),
            },
        },
        "pendencias": pendencias,
        "erro": None,
    }