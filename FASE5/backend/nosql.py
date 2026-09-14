import json
from pathlib import Path
from datetime import datetime


# Localização do banco NoSQL
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "cardioia_nosql.json"


def salvar_evento(evento):
    """
    Armazena um evento no banco NoSQL baseado em documentos JSON.
    """

    eventos = []

    # Recupera os eventos existentes
    if DB_PATH.exists():
        try:
            with open(DB_PATH, "r", encoding="utf-8") as arquivo:
                eventos = json.load(arquivo)
        except (json.JSONDecodeError, FileNotFoundError):
            eventos = []

    # Adiciona data/hora automaticamente
    evento["data_hora"] = datetime.now().isoformat()

    # Adiciona o novo documento
    eventos.append(evento)

    # Salva novamente o banco
    with open(DB_PATH, "w", encoding="utf-8") as arquivo:
        json.dump(eventos, arquivo, ensure_ascii=False, indent=4)

    return True


def buscar_eventos():
    """
    Retorna todos os eventos armazenados no banco NoSQL.
    """

    if not DB_PATH.exists():
        return []

    try:
        with open(DB_PATH, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except json.JSONDecodeError:
        return []


if __name__ == "__main__":
    evento_teste = {
        "tipo": "teste",
        "origem": "CardioIA",
        "mensagem": "Banco NoSQL funcionando"
    }

    salvar_evento(evento_teste)

    print("✅ Banco NoSQL funcionando!")
    print(f"📄 Arquivo: {DB_PATH}")
    print(f"📊 Eventos armazenados: {len(buscar_eventos())}")