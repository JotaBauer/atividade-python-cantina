i = 1
valor_compra = 0
print('Bem Vindo a nossa loja! Temos os seguintes produtos:')
while i == 1:

    print('\n')
    print('OPÇÂO|    PRODUTO    | PREÇO    ')
    print('  1  |  Suco         | R$5,00   ')
    print('  2  |  Salgado      | R$7,00   ')
    print('  3  |  Sanduíche    | R$10,00  ')
    print('  4  |  Finalizar Compra')
    print('\n')
    p = int(input('Digite um número: '))

    if p == 1:
        valor_compra+=5
    elif p == 2:
        valor_compra+=7
    elif p == 3:
        valor_compra+=10
    elif p == 4:
        print(f'O valor total da compra foi R$ {valor_compra}')
        break
    else:
        print('Opção invalida!')
        break

    q=str(input('Deseja comprar mais algo? [SIM/NAO]')).lower()
    if  q == 'sim':
        i = 1
    else:
        i = 0
        print(f'O valor total da compra foi R$ {valor_compra}')


