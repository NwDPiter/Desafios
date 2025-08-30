from pymongo import AsyncMongoClient
from configs.settings import settings


class MongoClient:
    def __init__(self) -> None:
        self.client: AsyncMongoClient = AsyncMongoClient(settings.DB_URL)

    async def get_client(self) -> AsyncMongoClient:
        # Opcional: conectar explicitamente
        await self.client.aconnect()
        return self.client


# Exemplo de uso
db_client = MongoClient()

# Em algum lugar do seu código assíncrono:
# async def usar_mongo():
#     client = await db_client.get_client()
#     db = client["meu_banco"]
#     colecao = db["minha_colecao"]
#     await colecao.insert_one({"nome": "Pedro"})
