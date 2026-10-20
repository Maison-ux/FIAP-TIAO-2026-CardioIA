from pydantic import BaseModel,Field
from typing import Any,Literal
class Erro(BaseModel):
    codigo:str
    mensagem:str
    agente_origem:str
class Envelope(BaseModel):
    versao_contrato:str="1.0"
    agente:str
    status:Literal["sucesso","parcial","erro"]
    caso_id:str
    resultado:dict[str,Any]=Field(default_factory=dict)
    pendencias:list[Any]=Field(default_factory=list)
    erro:Erro|None=None
