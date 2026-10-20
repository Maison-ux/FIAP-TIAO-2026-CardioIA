from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA_DIR=ROOT/"data"
ARTIFACTS_DIR=ROOT/"artifacts"
MODEL_PATH=ARTIFACTS_DIR/"random_forest_cardioia.joblib"
SEED=42
FEATURES=["idade_media","carga_sistema","tempo_espera","fc_media","spo2_media","pa_sistolica","temperatura","densidade_eventos","eventos_24h","disponibilidade_recursos"]
