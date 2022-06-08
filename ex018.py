#  Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
n = float(input('Digite um ângulo:'))
s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan((math.radians(n)))
#print('O seno do ângulo {} é {:2f} \n Cosseno é {:2} \n Tangente é {:2f}'.format(n, math.sin(n), math.cos(n), math.tan(n)))
print('Seno = {:1f} \n Cosseno = {:2f} \n Tangente = {:2f}'.format(s, c, t))


