#Exercicio 4.6


Escreva um programa que perguntea distancia que um passageiro deseja em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas


dist = int(input("Digite qual distância deseja percorrer : "))
if dist <= 200;
	novo_preco = dist * 0.50;
	print("Sua viagem fica no valor de %4.2f" %(novo_preco));
else:
	novo_preco = dist * 0.45;
	print("Sua viagem é bem longa, fica no valor de %4.2f" %(novo_preco));