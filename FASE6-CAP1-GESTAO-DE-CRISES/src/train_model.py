import json, joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report
from .config import FEATURES,SEED,ARTIFACTS_DIR,MODEL_PATH,DATA_DIR
from .data_generator import generate_dataset

def train_and_evaluate():
    df=generate_dataset()
    X,y=df[FEATURES],df["pico_risco"]
    Xtr,Xtmp,ytr,ytmp=train_test_split(X,y,test_size=.30,random_state=SEED,stratify=y)
    Xv,Xte,yv,yte=train_test_split(Xtmp,ytmp,test_size=.50,random_state=SEED,stratify=ytmp)
    model=RandomForestClassifier(n_estimators=300,random_state=SEED,class_weight="balanced",n_jobs=-1)
    model.fit(Xtr,ytr)
    def met(a,b):
        return {"accuracy":accuracy_score(a,b),"precision":precision_score(a,b,zero_division=0),"recall":recall_score(a,b,zero_division=0),"f1":f1_score(a,b,zero_division=0),"confusion_matrix":confusion_matrix(a,b).tolist(),"report":classification_report(a,b,output_dict=True,zero_division=0)}
    result={"seed":SEED,"n":len(df),"split":{"treino":len(Xtr),"validacao":len(Xv),"teste":len(Xte)},"distribuicao_classes":y.value_counts().sort_index().to_dict(),"validacao":met(yv,model.predict(Xv)),"teste":met(yte,model.predict(Xte)),"limitacao":"Dados sintéticos; não representa desempenho clínico."}
    ARTIFACTS_DIR.mkdir(exist_ok=True,parents=True); DATA_DIR.mkdir(exist_ok=True,parents=True)
    df.to_csv(DATA_DIR/"dados_sinteticos.csv",index=False)
    joblib.dump({"model":model,"features":FEATURES,"seed":SEED},MODEL_PATH)
    (ARTIFACTS_DIR/"metricas.json").write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding="utf-8")
    print(json.dumps(result,indent=2,ensure_ascii=False))
if __name__=="__main__": train_and_evaluate()
