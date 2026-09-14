from backend.ai_analysis import analisar_dados


def test_paciente_normal():
    dado = (1, 1, 120, 80, 72, 95)

    resultado = analisar_dados(dado)

    assert resultado["paciente"] == 1
    assert resultado["pressao"] == "120/80"
    assert resultado["frequencia_cardiaca"] == 72
    assert resultado["adesao"] == 95
    assert resultado["status"] == "NORMAL"
    assert resultado["alertas"] == []


def test_frequencia_cardiaca_elevada():
    dado = (2, 2, 120, 80, 110, 95)

    resultado = analisar_dados(dado)

    assert resultado["status"] == "ATENÇÃO"
    assert "Frequência cardíaca elevada" in resultado["alertas"]


def test_pressao_arterial_elevada():
    dado = (3, 3, 150, 95, 72, 95)

    resultado = analisar_dados(dado)

    assert resultado["status"] == "ATENÇÃO"
    assert "Pressão arterial elevada" in resultado["alertas"]


def test_baixa_adesao():
    dado = (4, 4, 120, 80, 72, 70)

    resultado = analisar_dados(dado)

    assert resultado["status"] == "ATENÇÃO"
    assert "Baixa adesão ao tratamento" in resultado["alertas"]


def test_multiplos_alertas():
    dado = (5, 5, 150, 95, 110, 70)

    resultado = analisar_dados(dado)

    assert resultado["status"] == "ATENÇÃO"
    assert len(resultado["alertas"]) == 3