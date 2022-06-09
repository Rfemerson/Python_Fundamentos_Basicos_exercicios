# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,
# 50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input('Qual a distância de sua  viagem?'))
if distancia <= 200:
    print('Sua passagem custa R$ {}'.format(distancia * 0.50))
else:
    print('Essa viagem é um pouco mais longa, sua passagem custa {}'.format(distancia * 0.45))
