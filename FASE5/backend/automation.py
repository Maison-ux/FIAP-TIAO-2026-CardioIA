from database.database import buscar_dados
from .ai_analysis import analisar_dados
from .nosql import salvar_evento


def executar_rpa():
    """
    Executa o fluxo automatizado do CardioIA.

    Fluxo:
    1. Consulta os dados clínicos no banco relacional.
    2. Analisa os dados utilizando o módulo de IA.
    3. Registra o resultado e os alertas no banco NoSQL.
    """

    print("🤖 RPA CardioIA iniciado...")
    print("🔎 Consultando dados clínicos...")

    dados = buscar_dados()

    if not dados:
        print("⚠️ Nenhum registro encontrado.")
        return []

    print(f"✅ {len(dados)} registro(s) encontrado(s).")
    print()

    resultados = []

    for dado in dados:

        print(
            f"Paciente {dado[1]} | "
            f"PA: {dado[2]}/{dado[3]} mmHg | "
            f"FC: {dado[4]} bpm | "
            f"Adesão: {dado[5]}%"
        )

        # Análise utilizando IA
        resultado = analisar_dados(dado)

        resultados.append(resultado)

        print(f"🧠 Análise da IA: {resultado['status']}")

        if resultado["alertas"]:
            for alerta in resultado["alertas"]:
                print(f"   ⚠️ {alerta}")
        else:
            print("   ✅ Nenhuma anomalia identificada.")

        # Registro no banco NoSQL
        evento = {
            "tipo": "analise_clinica",
            "origem": "CardioIA_RPA",
            "paciente": resultado["paciente"],
            "pressao": resultado["pressao"],
            "frequencia_cardiaca": resultado["frequencia_cardiaca"],
            "adesao": resultado["adesao"],
            "status": resultado["status"],
            "alertas": resultado["alertas"]
        }

        salvar_evento(evento)

        print("💾 Resultado registrado no banco NoSQL.")
        print()

    print("🏁 RPA finalizado.")

    return resultados


if __name__ == "__main__":
    executar_rpa()