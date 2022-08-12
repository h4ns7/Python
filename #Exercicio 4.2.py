#Exercicio 4.2

Condições


Escreva um programa que pergunte a velocidade do carro de um usuario. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo 
que o usuario foi multado. Neste caso, exiba o valor da multa, cobrando R$ 5,00 por km/h acima de 80km/h.



velocidade = int(input("Digite a valocidade de seu carro, por favor ! : "));
a_mais = velocidade - 80;
calc = a_mais * 5  + 80;
if velocidade > 80:
	print("Multa a pagar por excesso de velocidade R$%6.2f, pois ultrapassou %2.2d" %(calc, a_mais);