from pydantic import BaseModel
#from fastapi import UploadFile, File

class Produto(BaseModel):
    id_produto: int = None
    nome: str
    descricao: str = None
    valor_unitario: float
    foto: str = None