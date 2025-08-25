from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str
    DEBUG: bool = False
    HASH_PEPPER: str


    class Config :
        env_file = ".env"

settings = Settings()


###### Criptografia de senhas ######
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def create_hash(senha: str): # Senha + pepper(Funciona com um salt)
    senha_com_pepper = f'{senha}{settings.HASH_PEPPER}'
    return pwd_context.hash(senha_com_pepper)
