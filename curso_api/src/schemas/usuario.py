from typing import Annotated

from pydantic import BaseModel, EmailStr, Field


class UsuarioPOST(BaseModel):
    nome: Annotated[str, Field(description='Nome do atleta')]
    email: Annotated[EmailStr, Field(description='Email de login do user')]
    senha: Annotated[str, Field(description='Senha do user')]

    class Config:
        from_atributes = True

class UsuarioGET(BaseModel):
    id: Annotated[int, Field(description='Identificador do usuário')]
    nome: Annotated[str, Field(description='Nome do atleta',)]
    email: Annotated[EmailStr, Field(description='Email de login do user')]
    senha: Annotated[str, Field(description='Senha do user')]

    class Config:
        from_atributes = True

class UsuarioPUT(UsuarioPOST):
    id: Annotated[int, Field(description='Identificador do usuário')]


class UsuarioDELETE(BaseModel):
    email: Annotated[EmailStr, Field(description='Email de login do user')]
