# --- Registro de tabelas --- #
from sqlalchemy.orm import registry

reg = registry()
# --------------------------- #


# --- engine e criador de sessions --- #
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from tests.settings import settings

engine = create_async_engine(settings.DB_URL, echo=False)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
# --------------------------- #


# --- entregador de sessions --- #
from typing import AsyncGenerator


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
