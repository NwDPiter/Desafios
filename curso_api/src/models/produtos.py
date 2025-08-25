from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.base import reg


@reg.mapped_as_dataclass
class ProdutosModel:
    __tablename__ = 'produtos'

    id: Mapped[int] = mapped_column(Integer,init=False, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    descricao: Mapped[str] = mapped_column(String)
    quantidade: Mapped[str] = mapped_column(Integer, nullable=False)
    
