from agents import Agent

from ..tools import (
    consultar_protocolos,
    ferramenta_consultar_protocolos,
)


especialista_protocolos = Agent(
    name="Especialista em Protocolos",
    instructions=(
        "Você é o Especialista em Protocolos do CardioIA. "
        "Consulte as regras explícitas do enunciado. "
        "Não invente limiares nem ações. "
        "Preserve as pendências identificadas. "
        "Os dados são sintéticos e não devem ser utilizados "
        "para decisões clínicas reais."
    ),
    tools=[ferramenta_consultar_protocolos],
)


def avaliar(caso_id: str, dados_caso: dict) -> dict:
    """
    Retorna o resultado estruturado da consulta de protocolos.

    Preserva os protocolos acionados e as pendências no
    contrato JSON v1.0, sem depender de interpretação textual.
    """

    resultado = consultar_protocolos(caso_id, dados_caso)

    if resultado.get("status") == "erro":
        return resultado

    return resultado