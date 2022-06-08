# faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la
# sabendo que cada litro de tinta, pinta uma area de 2m quadrados
a = float(input('Qual a altura da parede que deseja pintar?'))
l = float(input('E qual a largura?'))
ar = a * l
t = ar / 2
print('A parede que deseja pintar tem {} metros quadrados e precisa de {}  litros de tinta para pintá-la'.format(ar, t))

