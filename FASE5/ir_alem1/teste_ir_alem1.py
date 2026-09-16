import json

from ai_generativa import (
    criar_prompt,
    estruturar_resposta,
    validar_saida,
    gerar_saida_simulada
)


def test_criar_prompt():
    texto = "Paciente apresenta palpitações há 30 minutos."
    prompt = criar_prompt(texto)

    assert "palpitações" in prompt
    assert "JSON válido" in prompt
    assert "Não invente informações" in prompt


def test_validar_saida():
    resultado = {
        "sintomas": ["palpitações"],
        "pressao_arterial": "150/95 mmHg",
        "frequencia_cardiaca": "110 bpm",
        "duracao": "aproximadamente 30 minutos",
        "medicamentos": ["medicamento para pressão"],
        "observacoes": None
    }

    assert validar_saida(resultado) is True


def test_estruturar_resposta():
    resposta = json.dumps({
        "sintomas": ["palpitações"],
        "pressao_arterial": "150/95 mmHg",
        "frequencia_cardiaca": "110 bpm",
        "duracao": "aproximadamente 30 minutos",
        "medicamentos": ["medicamento para pressão"],
        "observacoes": None
    }, ensure_ascii=False)

    resultado = estruturar_resposta(resposta)

    assert resultado["sintomas"] == ["palpitações"]
    assert resultado["pressao_arterial"] == "150/95 mmHg"
    assert resultado["frequencia_cardiaca"] == "110 bpm"


def test_saida_simulada():
    resposta = gerar_saida_simulada()
    resultado = estruturar_resposta(resposta)

    assert resultado["sintomas"] == ["palpitações"]
    assert resultado["pressao_arterial"] == "150/95 mmHg"
    assert resultado["frequencia_cardiaca"] == "110 bpm"
    assert resultado["duracao"] == "aproximadamente 30 minutos"
    assert resultado["medicamentos"] == ["medicamento para pressão"]
    assert resultado["observacoes"] is None