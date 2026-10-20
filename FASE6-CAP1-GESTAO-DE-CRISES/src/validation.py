import math
from .config import FEATURES
RANGES={"idade_media":(18,90),"carga_sistema":(30,100),"tempo_espera":(5,180),"fc_media":(50,150),"spo2_media":(70,100),"pa_sistolica":(80,200),"temperatura":(10,40),"disponibilidade_recursos":(20,100)}
INTS={"densidade_eventos","eventos_24h"}
def validate_case(d):
    if not isinstance(d,dict): return ["dados_caso deve ser objeto."]
    issues=[]
    for f in FEATURES:
        if f not in d: issues.append(f"Campo ausente: {f}"); continue
        v=d[f]
        if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v): issues.append(f"{f}: valor deve ser numérico e finito."); continue
        if f in RANGES and not RANGES[f][0]<=v<=RANGES[f][1]: issues.append(f"{f}: fora do intervalo {RANGES[f]}.")
        if f in INTS and (not float(v).is_integer() or v<0): issues.append(f"{f}: deve ser inteiro não negativo.")
    return issues
