# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
# mostre o comprimento da hipotenusa.
import math
from math import pow

ca = float(input('Olá! Qual a medida do cateto adjacente?'))
co = float(input('Agora me fala qual a medida do cateto oposto?'))
hi = math.hypot(ca, co)
#h = ca ** 2 + co ** 2 ** (1/2)
print('A hipotenusa do triângulo retangula em questão é {}'.format(hi))

