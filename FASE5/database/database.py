import sqlite3
from pathlib import Path


# Localização do banco de dados
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "cardioia.db"


def conectar():
    """Cria uma conexão com o banco SQLite."""
    return sqlite3.connect(DB_PATH)


def criar_tabela():
    """Cria a tabela de dados clínicos."""
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dados_clinicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paciente_id INTEGER NOT NULL,
            pressao_sistolica REAL NOT NULL,
            pressao_diastolica REAL NOT NULL,
            frequencia_cardiaca REAL NOT NULL,
            adesao_tratamento REAL NOT NULL,
            data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conexao.commit()
    conexao.close()


def inserir_dado(
    paciente_id,
    pressao_sistolica,
    pressao_diastolica,
    frequencia_cardiaca,
    adesao_tratamento
):
    """Insere um novo registro clínico."""
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO dados_clinicos (
            paciente_id,
            pressao_sistolica,
            pressao_diastolica,
            frequencia_cardiaca,
            adesao_tratamento
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        paciente_id,
        pressao_sistolica,
        pressao_diastolica,
        frequencia_cardiaca,
        adesao_tratamento
    ))

    conexao.commit()
    conexao.close()


def buscar_dados():
    """Retorna todos os dados clínicos cadastrados."""
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id,
            paciente_id,
            pressao_sistolica,
            pressao_diastolica,
            frequencia_cardiaca,
            adesao_tratamento,
            data_hora
        FROM dados_clinicos
        ORDER BY id
    """)

    dados = cursor.fetchall()

    conexao.close()

    return dados