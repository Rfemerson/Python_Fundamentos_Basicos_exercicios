# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Olá, tudo bem? Quantos kilometros você percorreu com nosso veículo?'))
d = int(input('Tudo bem, agora me informa quantos dias você ficou com ele?'))
v = (km * 0.15) + (d * 60)
print('Você percorreu {} km e ficou {} dias com nosso veículo,\n com isso o valor do aluguel do veiculo ficou R${:1f},'.format(km, d, v))
