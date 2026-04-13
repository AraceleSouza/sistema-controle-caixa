from time import sleep

print('{:=^40}'.format(' LOJINHA DA LULU '))

saldo = 0
totdinheiro = 0
totcartao = 0
totpix = 0

while True:
    try:
        compra = float(input('Digite o valor da compra: R$ '))
    except ValueError:
        print('❌ Valor inválido! Digite apenas números.')
        continue

    print('''FORMAS DE PAGAMENTO: 
[1] Dinheiro
[2] Cartão 
[3] Pix''')

    try:
        opcao = int(input('>>>>>> Qual a forma de pagamento? '))
    except ValueError:
        print('❌ Opção inválida!')
        continue

    if opcao == 1:
        totdinheiro += compra
        try:
            dinheiro = float(input('>>>>>> Qual valor pago? R$ '))
        except ValueError:
            print('❌ Valor inválido!')
            continue

        if dinheiro > compra:
            troco = dinheiro - compra
            print(f'\033[0;33mO valor da compra foi R${compra:.2f}, pagamento em DINHEIRO.')
            print(f'\033[0;33mTroco: R$ {troco:.2f}')
        elif dinheiro < compra:
            print('\033[0;33mAtenção! Valor insuficiente. Tente novamente!')
            continue
        else:
            print(f'\033[0;33mO valor da compra foi R${compra:.2f}, pagamento em DINHEIRO.')

        saldo += compra

    elif opcao == 2:
        cartao = input('>>>>>> Débito ou Crédito? [D/C] ').strip().upper()

        if cartao == 'C':
            acrescimo = compra * 0.05
            total = compra + acrescimo
            totcartao += total
            saldo += total

            print(f'\033[0;33mPagamento no CARTÃO DE CRÉDITO.')
            print(f'\033[0;33mValor original: R$ {compra:.2f}')
            print(f'\033[0;33mAcréscimo (5%): R$ {acrescimo:.2f}')
            print(f'\033[0;33mTotal: R$ {total:.2f}')

        elif cartao == 'D':
            totcartao += compra
            saldo += compra

            print(f'\033[0;33mPagamento no CARTÃO DE DÉBITO.')
            print(f'\033[0;33mTotal: R$ {compra:.2f}')

        else:
            print('\033[0;33mOpção inválida! Tente novamente!')
            continue

    elif opcao == 3:
        totpix += compra
        saldo += compra

        print(f'\033[0;33mPagamento via PIX.')
        print(f'\033[0;33mTotal: R$ {compra:.2f}')

    else:
        print('\033[0;33mOpção inválida! Tente novamente!')
        continue

    print('=-=' * 15)
    sleep(1)

    resp = input('\033[mNova compra? [S/N] ').strip().upper()
    if resp == 'N':
        break

print('Finalizando sistema...')
sleep(0.5)

print('~*' * 20)
print(f'\033[0;33mSALDO TOTAL DO CAIXA: R$ {saldo:.2f}')
print(f'\033[0;34mDinheiro: R$ {totdinheiro:.2f}')
print(f'\033[0;34mCartão: R$ {totcartao:.2f}')
print(f'\033[0;34mPix: R$ {totpix:.2f}')




