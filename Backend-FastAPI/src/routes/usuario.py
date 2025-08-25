from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr
from sqlalchemy import select

from src.db.base import AsyncSession, get_session
from src.models.usuario import UserModel
from src.schemas.usuario import UsuarioGET, UsuarioPOST
from tests.settings import create_hash

router = APIRouter()


@router.get('/listarUser', status_code=HTTPStatus.OK, response_model=list[UsuarioGET])
async def listar_users(db: AsyncSession = Depends(get_session)):
    try:
        # Uma consulta o bd que retorna tudo da tabela de users
        tabela_usuarios = await db.execute(select(UserModel))
        # Pega todos os itens da coluna
        usuarios = tabela_usuarios.scalars().all()
        return usuarios
    except Exception as erro:
        match erro:
            case ConnectionRefusedError():
                raise HTTPException(status_code=HTTPStatus.SERVICE_UNAVAILABLE, detail='Banco de dados fora do ar')


@router.post('/inserirUsers', status_code=HTTPStatus.CREATED, response_model=dict)
async def inserir_Users(user: UsuarioPOST , db: AsyncSession = Depends(get_session)):
    #Troca a senha do user por um hash
    senha_criptografada = create_hash(user.senha)

    # Desepacota o modelo que veio no payload para um que o banco entenda
    new_user = UserModel(
        nome = user.nome,
        email = user.email,
        senha = senha_criptografada
        )

    # Como é para inserir um user temos que fazer uma verificação no bd para saber se já existe
    tabela_email = await db.execute(select(UserModel).where(UserModel.email == new_user.email))

    # Pega o 1º valor da coluna
    usuario_existe = tabela_email.scalars().first()

    # Valida se existe
    if usuario_existe:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail='Email já cadastrado!')

    # caso não, inicia a adição ao banco
    else:
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return {'message':f'Usuário {new_user.nome} criado!'}


# Criar uma rota para atualizar cadastros
@router.put('/atualizarUser',status_code=HTTPStatus.OK, response_model=str)
async def atualizar_User(user: UsuarioPOST, db: AsyncSession = Depends(get_session)):
    try:

        senha_criptografada = create_hash(user.senha)

        # Vamos espera os conteúdo que o user que atualizar nesse caso {Nome, Email ou Senha}
        usuario_atualizado = UserModel(
            nome = user.nome,
            email = user.email,
            senha = senha_criptografada
            )

        # Fazer um select na tabela pelo email
        tabela_user = await db.execute(select(UserModel).where(UserModel.email == usuario_atualizado.email))

        # Pegar o 1º item da coluna
        usuario_existente = tabela_user.scalars().first()

    except Exception as e:
            print(e)
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='Valide os dados enviados')
    
    # Validar se user já existe
    if usuario_existente:
        # Se existir, faz a troca, sobrescrevendo o antigo pelo novo
        usuario_existente.nome = usuario_atualizado.nome
        usuario_existente.senha = usuario_atualizado.senha

        # Enviar para o banco
        await db.commit()
        await db.refresh(usuario_existente)
        return f'Usuário do email {usuario_atualizado.email} atualizado'

    else:
        # Se não, retorna um erro
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado')


# Criar um rota para fazer a exclução de usuários
@router.delete('/deletarUser', status_code=HTTPStatus.OK, response_model=str)
async def delete_user(email: EmailStr, db: AsyncSession = Depends(get_session)):
    # Fazer um select na tabela pelo email
    tabela_user = await db.execute(select(UserModel).where(UserModel.email == email))

    # Pegar o 1º item da coluna
    usuario_existente = tabela_user.scalars().first()

    if usuario_existente:
        await db.delete(usuario_existente)
        await db.commit()
        return f'Conta relacionada ao email {usuario_existente.email} foi deletada.'

    else:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado')
