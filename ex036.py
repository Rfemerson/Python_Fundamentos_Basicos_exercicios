# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
# o empréstimo será negado.
print('\033[34m=\033[m' * 30)
print('O SONHO DA CASA PROPRIA . LTDA')
print('\033[34m=\033[m' * 30)
Vc = float(input('Qual valor do imóvel que deseja?'))
s = float(input('Qual seu sálario atualmente? R$'))
t = int(input('Em quanto tempo deseja quitar o imóvel?'))
conversao = t * 12
Vp = Vc / conversao
if Vp > (s * 30) / 100:
    print('Infelizmente, não poderemos aprovar seu empréstimo.')
else:
    print('Parabêns!!! Seu empréstimo foi aprovado!')
    print('O valor da sua parcela mensal será de R$ %0.2f' % Vp)

