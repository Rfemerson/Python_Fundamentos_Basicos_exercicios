# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.
nome = str(input('Digite seu nome completo:')).strip()
n = nome.split()
print('Olá, {}! Esse é seu primeiro nome certo?'.format(n[0]))
print('Seu ultimo nome é {}'.format(n[len(n)-1]))






