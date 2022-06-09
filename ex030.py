# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Digite um número:'))
p = n % 2
if p == 0:
    print('O numero {} é Par'.format(n))
else:
    print('O número {} é impar'.format(n))
    
