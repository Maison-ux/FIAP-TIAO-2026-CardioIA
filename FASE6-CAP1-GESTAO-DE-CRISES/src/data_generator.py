import numpy as np
import pandas as pd
from .config import SEED, DATA_DIR

def generate_dataset(n=5000, seed=SEED):
    np.random.seed(seed)
    df=pd.DataFrame({
      "idade_media":np.random.normal(55,12,n).clip(18,90),
      "carga_sistema":np.random.uniform(30,100,n),
      "tempo_espera":np.random.normal(45,20,n).clip(5,180),
      "fc_media":np.random.normal(85,15,n).clip(50,150),
      "spo2_media":np.random.normal(95,3,n).clip(70,100),
      "pa_sistolica":np.random.normal(125,20,n).clip(80,200),
      "temperatura":np.random.normal(24,5,n).clip(10,40),
      "densidade_eventos":np.random.poisson(3,n),
      "eventos_24h":np.random.poisson(2,n),
      "disponibilidade_recursos":np.random.uniform(20,100,n)})
    score=((df.carga_sistema>80).astype(int)+(df.tempo_espera>60).astype(int)+(df.spo2_media<92).astype(int)+(df.fc_media>110).astype(int)+(df.eventos_24h>4).astype(int)+(df.disponibilidade_recursos<40).astype(int))
    df["pico_risco"]=(score>=2).astype(int)
    return df
if __name__=="__main__":
    DATA_DIR.mkdir(exist_ok=True,parents=True)
    generate_dataset().to_csv(DATA_DIR/"dados_sinteticos.csv",index=False)
