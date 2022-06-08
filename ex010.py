# crie um programa que leia quanto dinheiro tem na carteira e mostre quantos dolares ela pode comprar
# us$ 1 = R$ 3,27
n = float(input('Quanto você tem na carteira?'))
n1 = n / 3.27
print('Você pode comprar {:2f} dolares'.format(n1))
