#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
p = float(input('Qual valor do produto?'))
d = p - (p * 5 /100)
print('Valor do produto com desconto é {}'.format(d))
