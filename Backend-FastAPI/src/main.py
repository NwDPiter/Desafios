from fastapi import FastAPI

from src.routes.produtos import router as produtos
from src.routes.usuario import router as users

app = FastAPI(title='Doceria')

app.include_router(users, prefix='/api', tags=['Usuário'])
app.include_router(produtos, prefix='/api', tags=['Produtos'])
