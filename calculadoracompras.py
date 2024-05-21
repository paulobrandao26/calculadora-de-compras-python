preço = float(input('preço das compras: R$'))

print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] em até 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

opção: int = int(input('qual a opção?'))
dez = preço - (10/100 * preço)
cinco = preço - (5/100 * preço)

if opção == 1:
   print('sua compra foi a vista no valor de {:.2f}R$ e agora vai custar {:.2f}R$'.format(preço, dez))
elif opção == 2:
   print('sua compra a vista no cartão foi de {:.2f}R$ e agora vai custar {:.2f}R$'.format(preço, cinco))
elif opção == 3:
   parcela = int(input('Quantas parcelas?'))
   divisão = preço / parcela
   print('sua compra parcelada em {}x ficou R${:.2f}'.format(parcela, divisão))
else:
   valorTotal = (20/100 * preço) + preço
   parcela = int(input('Quantas parcelas?'))
   divisão = valorTotal/parcela
   print('sua compra parcelada em {}x ficou R${:.2f} com 20% de juros.'.format(parcela, divisão))