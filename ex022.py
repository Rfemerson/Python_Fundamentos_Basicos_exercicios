# Crie um programa que leia o nome completo de uma pessoa e mostre:
#
# – O nome com todas as letras maiúsculas e minúsculas.
#
# – Quantas letras ao todo (sem considerar espaços).
#
# – Quantas letras tem o primeiro nome.
nome = input('Olá, qual seu nome?')
# nome = str(input('Qual seu nome?')).split()
print('==== {} ===='.format(nome.upper()))
print('=== {} ==='.format(nome.lower()))
lista = nome.split()
print('Seu nome tem {} letras'.format(len(''.join(lista))))
print('Seu primeiro nome tem {} letras'.format(len(lista[0])))
