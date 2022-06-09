# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
s = float(input('Qual seu salário?'))
if s > 1250:
    aumento = s + (s * 10) / 100
if s <= 1250:
    aumento = s + (s * 15) / 100
print('O seú aumenro será de R$ {:2}'.format(aumento))
