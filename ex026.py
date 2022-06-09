# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela
# aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase:')).strip()
x = frase.upper()
print('A frase tem {} letra A'.format(x.count('A')))
print('A primeira vez que a letra A aparece é na posição {}'.format(x.find('A')))
print('A ultima vez que a letra A aparece é na posição {}'.format(x.rfind('A')))
