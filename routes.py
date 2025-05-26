from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from typing import List, Optional

from app.database import get_db
from app.models import Produto
from app.schemas import ProdutoCreate, ProdutoUpdate, ProdutoResponse

router = APIRouter()

@router.post("/produtos", response_model=ProdutoResponse, status_code=status.HTTP_201_CREATED)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo = Produto(**produto.dict(exclude_unset=True))
    try:
        db.add(novo)
        db.commit()
        db.refresh(novo)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Erro ao criar produto: dados inválidos ou duplicados.")
    return novo

@router.patch("/produtos/{produto_id}", response_model=ProdutoResponse)
def atualizar_produto(produto_id: int, dados: ProdutoUpdate, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    for key, value in dados.dict(exclude_unset=True).items():
        setattr(produto, key, value)
    
    if 'updated_at' not in dados.dict(exclude_unset=True):
        produto.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(produto)
    return produto

@router.get("/produtos", response_model=List[ProdutoResponse])
def listar_produtos(
    price_min: Optional[float] = Query(None, alias="price_min"),
    price_max: Optional[float] = Query(None, alias="price_max"),
    db: Session = Depends(get_db)
):
    query = db.query(Produto)
    if price_min is not None:
        query = query.filter(Produto.preco > price_min)
    if price_max is not None:
        query = query.filter(Produto.preco < price_max)
    return query.all()