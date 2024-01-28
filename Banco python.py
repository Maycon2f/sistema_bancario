

saldo = 500
limite_diario = 3
extrato = [[],[]]

while True:
    menu = str(input(' Boas Vindas ao banco PYTHON.\n Escolha uma opção:\n 1-|Saque \n 2-|Depósito \n 3-|Limite \n 4-|Extrato \n 0-|Sair\n'))
    opcao = menu.isnumeric()
    if opcao == True:
        menu = int(menu)
        if menu == 1:
            if limite_diario == 0:
                print('-+' * 30)
                print('Você alcançou o seu limite diário de saque!')
                print('-+' * 30)
            else:
                if menu == 1:
                    print('-+' * 30)
                    valor = int(input('Qual o valor que você deseja sacar?: '))

                    if valor > saldo:
                        print('-+' * 30)
                        print(f'Você não tem R${valor:.2f}  disponivel em conta para sacar. Valor disponivel R${saldo:.2f}')

                    elif valor <= 0:
                        print('-+' * 30)
                        print('Valor de saque invalido.')

                    elif saldo == 0:
                        print('-+' * 30)
                        print('Você não possui saldo disponível em conta para sacar.')

                    else:
                        saldo -= valor
                        print('-+' * 30)
                        print(f'Você realizou o saque de R${valor:.2f}, valor em conta R${saldo:.2f}')
                        limite_diario -= 1
                        valor = str(valor)
                        extrato[1].append(f'Saque: R$' + valor)
                print('-+' * 30)

        if menu == 2:
            valor = float(input('Qual valor você gostaria de depositar?: '))
            saldo += valor
            print('-+' * 30)
            print(f'Você depositou o valor de R$ {valor:.2f}. Saldo em conta:R$ {saldo:.2f}')
            print('-+' * 30)
            valor = str(valor)
            extrato[0].append('Deposito: R$' + valor)
        
        if menu == 3:
            print('-+' * 30)
            print(f'Você ainda pode sacar {limite_diario} veze(s)')
            print('-+' * 30)

        if menu == 4:
            print('-+' * 30)
            print('Extrato'.center(60, '='))
            for deposito in extrato[0]:
                print(deposito)

            for saque in extrato[1]:
                print(saque)
            print('=' * 60)
            print(f'Saldo em conta R${saldo:.2f}')

            print('-+' * 30)
        if menu == 0:
           print('-+' * 30)
           print('Saindo...')
           break 
    else: 
        print('-+' * 30)
        print('Digite uma opção valida')
        print('-+' * 30)