def analisar_dados(dado):
    """
    Analisa os dados clínicos do paciente e identifica
    possíveis situações de atenção.
    """

    paciente = dado[1]
    pressao_sistolica = dado[2]
    pressao_diastolica = dado[3]
    frequencia_cardiaca = dado[4]
    adesao = dado[5]

    alertas = []

    # Análise da frequência cardíaca
    if frequencia_cardiaca > 100:
        alertas.append("Frequência cardíaca elevada")

    elif frequencia_cardiaca < 60:
        alertas.append("Frequência cardíaca baixa")

    # Análise da pressão arterial
    if pressao_sistolica >= 140 or pressao_diastolica >= 90:
        alertas.append("Pressão arterial elevada")

    # Análise da adesão ao tratamento
    if adesao < 80:
        alertas.append("Baixa adesão ao tratamento")

    # Resultado final
    if alertas:
        status = "ATENÇÃO"
    else:
        status = "NORMAL"

    resultado = {
        "paciente": paciente,
        "pressao": f"{pressao_sistolica}/{pressao_diastolica}",
        "frequencia_cardiaca": frequencia_cardiaca,
        "adesao": adesao,
        "status": status,
        "alertas": alertas
    }

    return resultado