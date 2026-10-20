from src.data_generator import generate_dataset
from src.validation import validate_case
from src.config import FEATURES
def test_dataset_size_and_features():
    d=generate_dataset(); assert len(d)==5000 and "pico_risco" in d
    assert all(f in d for f in FEATURES)
def test_valid_case():
    d=generate_dataset(n=1).iloc[0].to_dict(); d.pop("pico_risco")
    assert validate_case(d)==[]
def test_missing_feature_rejected():
    d=generate_dataset(n=1).iloc[0].to_dict(); d.pop("pico_risco"); d.pop("fc_media")
    assert validate_case(d)
