from pydantic import BaseModel, Field
from typing_extensions import Annotated


class ProdutoIn(BaseModel):
    nome: Annotated[str,Field(description='Nome do produto')]
    quantidade: Annotated[int,Field(description='Quantidade de itens')]
    descricao: Annotated[str, Field(description='Descrição para detalhes')]

class ProdutoOut(BaseModel):
    #id: Annotated[int, Field(description='Identificador do produto')]
    nome: Annotated[str,Field(description='Nome do produto')]
    quantidade: Annotated[int,Field(description='Quantidade de itens')]
    descricao: Annotated[str, Field(description='Descrição para detalhes')]

class ProdutoDel(BaseModel):
    nome: Annotated[str,Field(description='Nome do produto')]


    class Config:
        from_attributes = True
