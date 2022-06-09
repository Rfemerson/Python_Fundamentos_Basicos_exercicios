# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo.
print('Vamos formar um triângulo? Preciso que me informe o comprimento das restas')
n1 = float(input('Primeira reta:'))
n2 = float(input('Segunda reta:'))
n3 = float(input('Terceira reta:'))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n3:
    print('Temos um tirângulo!')
else:
    print('Não temos um triângulo!')



