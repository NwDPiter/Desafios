# MENU
def func_menu():
    opcao = input("""
    [D] - Deposito
    [S] - Saque
    [E] - Extrato
    [CN] - Criar novo usuário  
    [LU] - Listar usuários
    [CB] - Criar conta bancária
    [LC] - Listar contas bancárias
    [Q] - Sair
                    
    Escolha sua opção:
    """)
    return opcao

###########[DEPÓSITO, SAQUE e EXTRATO]###########{

# DEPÓSITO (OK)
def func_deposito(valor_deposito, saldo, extrato):
    extrato = f'Depósito: R$ {valor_deposito:.2f}\n'
    saldo += valor_deposito
    print('Saque realizado com  sucesso')
    return extrato, saldo

# SAQUE (OK)
def func_saque(*, quantidade_saques, extrato, saldo, limite_saque, valor_saque):

    if quantidade_saques >= limite_saque:
        print('@@@Limite de saques diários excedido@@@')

    elif quantidade_saques > saques_feitos and valor_saque > saldo:
            print('@@@Saldo insuficiente@@@')

    elif valor_saque > limite_saque:
            print('@@@Valor máximo de saque: 500 reais@@@')

    elif valor_saque <= 500:
            extrato += f'Saque: R$ {valor_saque:.2f}\n'
            saldo -= valor_saque 
            saques_feitos += 1
            print('Saque realizado com  sucesso')

    return extrato, saldo

# EXTRATO (OK)
def func_extrato(saldo, / , *, extrato):
    print('#####Extrato#####')
    print(extrato)
    print(f'Saldo: R$ {saldo:.2f}')
    print('#####Extrato#####')

###########[DEPÓSITO, SAQUE e EXTRATO]###########}



###########[CRIAR, VALIDAR, LISTAR(USUÁRIOS e CONTAS)]###########{

# Crate user (OK)
def criar_usuario(nome, data_nascimento, cpf, endereco):
    return {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'cpf': cpf,
            'endereço': endereco,
            }

# Criar conta bancária (OK)
def criar_conta(BDusers, BDcontas):
    cpf = str(input('Informe seu cpf (Apenas os números): ').strip())
    cpfs_existentes = [pessoas["cpf"] for pessoas in BDusers]
    if cpf in cpfs_existentes:
        print('Conta bancária criada com sucesso.')
        return {
                'agencia': '0001',
                'numero_conta': len(BDcontas) + 1,
                'usuario': cpf
               }
    else:
        print('CPF não cadastrado!')

# Validar cpf (OK)
def validar_cpf(users):
    while True:
        cpf = input('Informe seu cpf (Apenas os números): ').strip()
        cpfs_existentes = [pessoas["cpf"] for pessoas in users]
        if cpf in cpfs_existentes:
            print('CPF inválido')
        else:    
            return cpf

# Listar Users (OK)
def listar_users(users):
    for pessoas in users:
        print(f'{pessoas}')

# Listar contas bancárias (OK)
def listar_conta_bancaria(contas):
    for pessoas in contas:
        print(f'{pessoas}')

###########[CRIAR, VALIDAR, LISTAR(USUÁRIOS e CONTAS)]###########}

# Função principal (Chama as outras funções)
def main():
    QUANTIADADE_SAQUES = 3
    AGENCIA = '0001'
    saldo = 0
    limite = 500
    extrato = ''
    users = []
    contas = []

    while True:
        opcao = func_menu()

        if opcao.upper() == 'Q':
            break

        elif opcao.upper() == 'D': # DEPÓSITO
            valor = float(input('Informe o valo do depósito: '))
            extrato, saldo = func_deposito(valor, saldo, extrato)
            
        elif opcao.upper() == 'S': # SAQUE

            valor = float(input('Informe o valo do saque: '))
            extrato, saldo = func_saque(quantidade_saques=QUANTIADADE_SAQUES, extrato=extrato, saldo=saldo, limite_saque=limite, valor_saque=valor)

        elif opcao.upper() == 'E': # EXTRATO
            func_extrato(saldo, extrato=extrato)

        elif opcao.upper() == 'CN': # CRIAR USUÁRIO
            nome = input('Informe seu nome: ')
            data_nascimento = input('Informe sua data de nascimento (Ex: dd/mm/aaaa): ')
            cpf = validar_cpf(users)
            endereco = input('Informe seu endereço (Logradouro - Bairro - Cidade/Sigla): ')
            usuario = criar_usuario(nome, data_nascimento, cpf, endereco)
            users.append(usuario)
            print('Usuário criado')

        elif  opcao.upper() == 'CB': # CRIAR CONTA BANCÁRIA
            conta_user = criar_conta(users, contas)
            contas.append(conta_user)

        elif opcao.upper() == 'LU': # LISTAR USUÁRIOS
            listar_users(users)

        elif opcao.upper() == 'LC': # LISTAR CONTAS BANCÁRIAS
            listar_conta_bancaria(contas)

        else:
            print('Informe um opcão válida')

main() 


