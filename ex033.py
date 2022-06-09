# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('Vamos descobrir qual número é o maior!')
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('DIgite o segundo número:'))
n3 = int(input('Digite o segundo número:'))
menor = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O maior número digitado foi {} '.format(maior))
print('O menor número digitado foi {}'.format(menor))
