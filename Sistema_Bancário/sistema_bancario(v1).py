# Variáveis
saldo = 1500
deposito = 0
saque = 0
extrato = ""
QUANTIDADE_SAQUES = 3

# Laço
while True:

    opcao = input("""
1 - Deposito
2 - Saque
3 - Extrato
0 - Sair
                  
Escolha sua opção:
""")

    # Saida do sistema
    if opcao == '0':
        break

    # Opção de Depósito
    if opcao == '1':
        valor_deposito = float(input('Digite o valor para depósito: '))
        extrato = f'Depósito: R$ {valor_deposito:.2f}\n'
        saldo += valor_deposito

    #Opção de Saque
    elif opcao == '2':
        if QUANTIDADE_SAQUES == 0:
            print('Limite de saques diários excedido')

        elif QUANTIDADE_SAQUES > 0:
            valor_saque = float(input('Digite o valor para saque: '))
            if valor_saque > saldo:
                    print('Saldo insuficiente')

            elif valor_saque > 500:
                    print('Valor máximo de saque: 500 reais')

            elif valor_saque <= 500:
                extrato += f'Saque: R$ {valor_saque:.2f}\n'
                saldo -= valor_saque 

            quantidade_saques -= 1

    #Opção de Extrato
    elif opcao == '3':
        print('#####Extrato#####')
        print(extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('#####Extrato#####')
        
    #Opção incorreto
    else:
        print('Selecione uma opção existente!')         

