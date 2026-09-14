from database.database import criar_tabela, inserir_dado, buscar_dados
from backend.automation import executar_rpa


def main():
    print("🫀 CardioIA — Fase 5")
    print("=" * 45)

    # 1. Inicialização do banco
    print("🗄️ Inicializando banco de dados...")
    criar_tabela()

    # 2. Verifica se já existem dados
    dados = buscar_dados()

    # Insere um dado de teste somente se o banco estiver vazio
    if not dados:
        print("➕ Inserindo dados clínicos de teste...")

        inserir_dado(
            paciente_id=1,
            pressao_sistolica=120,
            pressao_diastolica=80,
            frequencia_cardiaca=72,
            adesao_tratamento=95
        )

    else:
        print(f"📋 {len(dados)} registro(s) clínico(s) já existente(s).")

    print()

    # 3. Executa o fluxo automatizado
    print("🤖 Iniciando processamento automatizado...")
    print()

    resultados = executar_rpa()

    # 4. Resumo final
    print()
    print("=" * 45)
    print("📊 RESUMO DA EXECUÇÃO")
    print("=" * 45)
    print(f"Registros processados: {len(resultados)}")

    for resultado in resultados:
        print(
            f"Paciente {resultado['paciente']} | "
            f"Status: {resultado['status']} | "
            f"Alertas: {len(resultado['alertas'])}"
        )

    print("=" * 45)
    print("✅ CardioIA — Fase 5 finalizada.")


if __name__ == "__main__":
    main()