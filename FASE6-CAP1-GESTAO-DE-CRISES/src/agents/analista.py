import json

from dotenv import load_dotenv
from agents import Agent, Runner

from ..tools import ferramenta_prever_risco


load_dotenv()


analista_risco = Agent(
    name="Analista de Risco",
    instructions=(
        "Você é o Analista de Risco do CardioIA. "
        "Utilize a ferramenta ferramenta_prever_risco para analisar "
        "os dados recebidos. Preserve o resultado retornado pela "
        "ferramenta e não invente valores. "
        "O score não representa uma probabilidade clínica calibrada. "
        "Os dados são sintéticos e não devem orientar decisões clínicas."
    ),
    tools=[ferramenta_prever_risco],
)


def analisar(caso_id: str, dados_caso: dict) -> dict:
    """Executa o agente e preserva o contrato retornado pela ferramenta."""

    entrada = (
        f"Analise o caso {caso_id}. "
        "Passe os dados abaixo para a ferramenta como JSON.\n"
        f"{json.dumps(dados_caso, ensure_ascii=False)}"
    )

    try:
        execucao = Runner.run_sync(
            analista_risco,
            input=entrada,
        )

        # Recupera o resultado estruturado da ferramenta utilizada.
        for item in reversed(execucao.new_items):
            if type(item).__name__ == "ToolCallOutputItem":
                saida_ferramenta = getattr(item, "output", None)

                if not isinstance(saida_ferramenta, str):
                    raise ValueError(
                        "A ferramenta não retornou uma saída textual JSON."
                    )

                resultado = json.loads(saida_ferramenta)

                if not isinstance(resultado, dict):
                    raise ValueError(
                        "A saída da ferramenta não é um objeto JSON."
                    )

                # Preserva o contrato original, inclusive erros e pendências.
                resultado["caso_id"] = caso_id
                resultado["agente"] = "Analista de Risco"

                return resultado

        return {
            "versao_contrato": "1.0",
            "agente": "Analista de Risco",
            "status": "erro",
            "caso_id": caso_id,
            "resultado": {},
            "pendencias": [],
            "erro": {
                "codigo": "FERRAMENTA_NAO_EXECUTADA",
                "mensagem": (
                    "A execução do agente terminou sem uma saída "
                    "identificável da ferramenta de previsão."
                ),
                "agente_origem": "Analista de Risco",
            },
        }

    except Exception as erro:
        return {
            "versao_contrato": "1.0",
            "agente": "Analista de Risco",
            "status": "erro",
            "caso_id": caso_id,
            "resultado": {},
            "pendencias": [],
            "erro": {
                "codigo": "ANALISE_FALHOU",
                "mensagem": str(erro),
                "agente_origem": "Analista de Risco",
            },
        }