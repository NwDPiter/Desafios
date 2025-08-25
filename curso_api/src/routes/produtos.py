from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select

from src.db.base import AsyncSession, get_session
from src.models.produtos import ProdutosModel
from src.schemas.produtos import ProdutoIn, ProdutoOut, ProdutoDel

router = APIRouter()


# Criando rota para visualizar os produtos adicionardos no banco
@router.get('/listarProdutos', status_code=HTTPStatus.OK, response_model=list[ProdutoOut])
async def listar_produtos(db: AsyncSession = Depends(get_session)):

    # Faz uma consulta para a tabela inteira ``SELECT * FROM ProdutosModel``
    stmt = await db.execute(select(ProdutosModel))
    all_products = stmt.scalars().all()

    # Validar se tem algum produto
    if all_products:
        return all_products
    else:
        raise HTTPException(HTTPStatus.NOT_FOUND, detail='Não há produtos cadastrados')


# Para inserir algo no banco primeiro precisamos validar se o obejto já existe
@router.post('/inserirProdutos', status_code=HTTPStatus.OK, response_model=dict)
async def inserir_produtos(produto: ProdutoIn, db: AsyncSession = Depends(get_session)):

    # Desconpactar para modelo ORM (Pydantic ->SQLAlchemy)
    new_produto = ProdutosModel(**produto.model_dump())

    # Fez uma consulta na tabela de produtos para a coluna de nome, onde o nome que veio pelo payload e == ao que está no bd
    coluna_nome_produtos = await db.execute(select(ProdutosModel).where(ProdutosModel.nome == new_produto.nome))

    # Pega o primeiro item da coluna
    produto_existe = coluna_nome_produtos.scalars().first()

    # Validando se produto já existe, caso sim, retornar um erro, caso não, adicionar no banco
    if produto_existe:
        raise HTTPException(HTTPStatus.CONFLICT, detail='Produto já cadastrado')

    # Uso sem o else no user e funcionar
    else:
        db.add(new_produto)
        await db.commit()
        await db.refresh(new_produto)
        return {'message': f'Produto {produto.nome} adicionado'}


# Criar uma rota para atualizar produtos
@router.put('/atualizarProdutos', status_code=HTTPStatus.OK, response_model=str)
async def atualizar_produto(produto: ProdutoIn, db: AsyncSession = Depends(get_session)):
    try:
        produto_atualizado = ProdutosModel(**produto.model_dump())
        # 1º vamos validar se esse produto já existe:
        tabela_produto = await db.execute(select(ProdutosModel).where(ProdutosModel.nome==produto_atualizado.nome))
        produto_existente = tabela_produto.scalars().first()

    except Exception as e:
            print(e)
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='Valide os dados enviados')
            
    if produto_existente:       
        # Jà vai ter os campo preenchindo com o conteúdo anterio só vai mudar o campo necessário 
        produto_existente.nome = produto_atualizado.nome
        produto_existente.descricao = produto_atualizado.descricao
        produto_existente.quantidade = produto_atualizado.quantidade

        # Depois de atribuir os novos campos vamos fazer o envio para o db        
        await db.commit()
        await db.refresh(produto_existente)
        return f'Produto atualizado.'

    else:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Produto inexistente.')


# Criar um rota para fazer a exclução de produtos
@router.delete('/deletarProdutos', status_code=HTTPStatus.OK, response_model=str)
async def deletar_produto(produto: ProdutoDel, db: AsyncSession = Depends(get_session)):

    # Cosultar ao banco produto no banco
    tabela_de_produtos = await db.execute(select(ProdutosModel).where(ProdutosModel.nome==produto.nome))

    # Pegar o 1º item da coluna
    produto_existente = tabela_de_produtos.scalars().first()

    # Validar se produto existe
    if produto_existente:
        await db.delete(produto_existente)
        await db.commit()
        return f'Produto deletado com sucesso.'

    else:
        raise HTTPException(HTTPStatus.NOT_FOUND, detail='Produto especificado não encontrado')