# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
v = float(input('Qual velocidade você estava?'))
l = 80
m = (v - l) * 7
if v < l:
    print('Muito bem! Você estava dentro do limite de velocidade.')
else:
    print('Você ultrapassou o limite de velocidade!')
    print('Você passou com {} km/h em uma via de {} km/h'.format(v, l))
    print('Sua multa custará {} reais'.format(m))

