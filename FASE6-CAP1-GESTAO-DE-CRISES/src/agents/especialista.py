from agents import Agent

from ..tools import (
    consultar_protocolos,
    ferramenta_consultar_protocolos,
)
from .planejador import planejador_resposta


especialista_protocolos = Agent(
    name="Especialista em Protocolos",
    instructions=(
        "Você é o Especialista em Protocolos do CardioIA.\n\n"

        "TAREFA OBRIGATÓRIA:\n"
        "1. Identifique o caso e os dados originais do paciente "
        "recebidos na conversa.\n"
        "2. Antes de transferir o controle, chame obrigatoriamente "
        "a ferramenta ferramenta_consultar_protocolos.\n"
        "3. Passe o identificador original em caso_id.\n"
        "4. Passe todos os dados originais do paciente, serializados "
        "como uma string JSON, no argumento dados_json.\n"
        "5. Aguarde o resultado da ferramenta.\n"
        "6. Preserve os protocolos acionados e as pendências "
        "retornadas pela ferramenta.\n"
        "7. Após obter o resultado, transfira o controle ao "
        "Planejador de Resposta usando o handoff disponível.\n\n"

        "Não invente protocolos, resultados, limiares ou valores. "
        "Não encaminhe o caso ao Planejador antes de consultar "
        "a ferramenta. "
        "O limiar de risco sistêmico alto não foi especificado "
        "no enunciado e deve permanecer como pendência. "
        "Os dados são sintéticos e não devem orientar decisões "
        "clínicas reais."
    ),
    tools=[ferramenta_consultar_protocolos],
    handoffs=[planejador_resposta],
)


def avaliar(caso_id: str, dados_caso: dict) -> dict:
    """
    Mantém a função determinística utilizada pelo fluxo
    tradicional do projeto.
    """
    return consultar_protocolos(
        caso_id=caso_id,
        dados_caso=dados_caso,
    )