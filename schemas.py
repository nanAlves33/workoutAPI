from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProdutoCreate(BaseModel):
    nome: str
    preco: float
    updated_at: Optional[datetime] = None

class ProdutoUpdate(BaseModel):
    nome: Optional[str]
    preco: Optional[float]
    updated_at: Optional[datetime]

class ProdutoResponse(BaseModel):
    id: int
    nome: str
    preco: float
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True