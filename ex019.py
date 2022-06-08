# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
nome1 = input('Qual nome do primeiro alunos?')
nome2 = input('Qual nome do segundo aluno?')
nome3 = input('Qual nome do terceiro aluno?')
nome4 = input('Qual nome do quarto aluno?')
#lista = [nome1, nome2, nome3, nome4]
#Escolhido = random.choice(lista)
#print('O aluno escolhido para ajudá-lo é: {}'.format(Escolhido))
print('O aluno sorteado para ajudá-lo é: {}'.format(random.choice([nome1])))

