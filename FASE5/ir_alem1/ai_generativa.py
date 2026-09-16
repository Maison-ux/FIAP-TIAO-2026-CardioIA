import json
from typing import Dict, Any


def criar_prompt(texto_clinico: str) -> str:
    """
    Cria um prompt estruturado para extração de informações clínicas.
    """

    return f"""
Você é um assistente de processamento de informações clínicas
para fins exclusivamente acadêmicos.

Analise o texto clínico abaixo e extraia somente as informações
explicitamente mencionadas.

Retorne exclusivamente um JSON válido com os campos:

{{
    "sintomas": [],
    "pressao_arterial": null,
    "frequencia_cardiaca": null,
    "duracao": null,
    "medicamentos": [],
    "observacoes": null
}}

Não invente informações ausentes no texto.

Texto clínico:
{texto_clinico}
""".strip()


def validar_saida(resultado: Dict[str, Any]) -> bool:
    """
    Verifica se a resposta possui a estrutura esperada.
    """

    campos_obrigatorios = {
        "sintomas",
        "pressao_arterial",
        "frequencia_cardiaca",
        "duracao",
        "medicamentos",
        "observacoes"
    }

    return campos_obrigatorios.issubset(resultado.keys())


def estruturar_resposta(resposta: str) -> Dict[str, Any]:
    """
    Converte uma resposta JSON da IA em um dicionário Python
    e valida sua estrutura.
    """

    try:
        resultado = json.loads(resposta)
    except json.JSONDecodeError as erro:
        raise ValueError(
            "A resposta recebida não é um JSON válido."
        ) from erro

    if not validar_saida(resultado):
        raise ValueError(
            "A resposta não possui todos os campos esperados."
        )

    return resultado

def gerar_saida_simulada() -> str:
    """
    Simula uma resposta de IA Generativa para fins acadêmicos.
    A estrutura representa o resultado esperado da extração clínica.
    """
    return json.dumps(
        {
            "sintomas": ["palpitações"],
            "pressao_arterial": "150/95 mmHg",
            "frequencia_cardiaca": "110 bpm",
            "duracao": "aproximadamente 30 minutos",
            "medicamentos": ["medicamento para pressão"],
            "observacoes": None
        },
        ensure_ascii=False
    )

if __name__ == "__main__":
    caminho_entrada = "ir_alem1/entrada_clinica.txt"

    with open(caminho_entrada, "r", encoding="utf-8") as arquivo:
        texto_clinico = arquivo.read().strip()

    prompt = criar_prompt(texto_clinico)

    print("🫀 CardioIA — IR ALÉM 1")
    print("=" * 50)
    print("\n📄 TEXTO CLÍNICO:\n")
    print(texto_clinico)

    print("\n🧠 PROMPT PARA IA GENERATIVA:\n")
    print(prompt)

    print("\n✅ Entrada clínica carregada e prompt preparado.")

    resposta_ia = gerar_saida_simulada()
    resultado = estruturar_resposta(resposta_ia)

    with open(
        "ir_alem1/saida_clinica.json",
        "w",
        encoding="utf-8"
    ) as arquivo:
        json.dump(
            resultado,
            arquivo,
            ensure_ascii=False,
            indent=4
        )

    print("\n✅ Extração clínica estruturada com sucesso.")
    print("📄 Saída salva em: ir_alem1/saida_clinica.json")