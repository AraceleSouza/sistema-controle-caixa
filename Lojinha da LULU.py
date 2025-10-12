print('{:=^40}'.format(' LOJINHA DA LULU '))
from time import sleep
opção = saldo = totdinheiro = totcartão = totpix = 0
resp = 'Ss'
while resp in 'Ss':
    compra = float(input('Digite o valor da compra:R$ '))
    print('''FORMAS DE PAGAMENTO: 
[1]Dinheiro
[2]Cartão 
[3]Pix''')
    opção = int(input('>>>>>> Qual a forma de pagamento? '))
    if opção == 1:
        totdinheiro = totdinheiro + compra
        dinheiro = float(input('>>>>>> Qual valor pago? R$'))
        if dinheiro > compra:
            troco = dinheiro - compra
            print('\033[0;33mO valor da compra foi R${}, pagamento em DINHEIRO.'.format(compra))
            print('\033[0;33mDiferença(troco) R$ {:.2f}.'.format(troco))
        elif dinheiro < compra:
            print('\033[0;33mAtenção! Valor do pagamento abaixo do valor da compra.TENTE NOVAMENTE!')
        elif compra == dinheiro:
            print('\033[0;33mO valor da compra foi R${}, pagamento em DINHEIRO.'.format(compra))
    elif opção == 2:
        cartão = str(input('>>>>>> Débito ou Crédito? [D/C]')).strip().upper()[0]
        if cartão == 'C':
            totcartão = totcartão + compra
            acréscimo = compra + (compra*5/100)
            print('\033[0;33mO valor da compra foi R${}, pagamento no CARTÃO de CRÉDITO.'.format(compra))
            print('\033[0;33mAcréscimo de 5% no valor de R${}. Valor total da compra R${}'.format(compra * 5 / 100, acréscimo))
        elif cartão == 'D':
            totcartão = totcartão + compra
            print('\033[0;33mO valor da compra foi R${}, pagamento no CARTÃO de DÉBITO.'.format(compra))
        else:
            print('\033[0;33mOpção INVÁLIDA! Tente novamente!')
    elif opção == 3:
        totpix = totpix + compra
        print('\033[0;33mO valor da compra foi R${}, pagamento no PIX.'.format(compra))
    else:
        print('\033[0;33mOpção INVÁLIDA! Tente novamente!')
    print('=-=' * 15)
    sleep(1)
    saldo = saldo + compra
    resp = str(input('\033[mNova Compra? [S/N]')).upper().strip()[0]
print('Finalizando Sistema...')
sleep(0.5)
print('~*' * 20)
print('\033[0;33mSALDO TOTAL DO CAIXA: R${:.2f}'.format(saldo))
print('\033[0;34mDinheiro: R${}'.format(totdinheiro))
print('\033[0;34mCartão: R${}'.format(totcartão))
print('\033[0;34mPix: R${}'.format(totpix))




