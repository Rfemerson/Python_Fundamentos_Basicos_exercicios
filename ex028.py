# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
# perdeu.
# print('Quero ver se você é bom de advinhação')
# n = int(input('Estou pensando em um numero! Qual número estou pensando?'))
# if 3 == n:
  #  print('Você é muito bom nisso hien! Parabéns')
# else:
 #   print('É pequeno gafanhoto, não foi dessa vez')
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5, tente adivinhar')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei?'))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns, você me venceu! Eu pensei no número {}'.format(computador))
else:
    print('Eu ganhei! Quem sabe você consegue na proxima. Eu pensei no número {} e você no número {}'.format(computador,jogador))


