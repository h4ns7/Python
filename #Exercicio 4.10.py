#Exercicio 4.10

Escreva uma programa que calcule o preço a pagar pelo fornecimento de energia eletrica.Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residencias, 
I para industrias e C para comercios. Calcule o preço a pagar de acordo com a tebela a seguir : 



instalacao_tipo = input("Qual tipo de instalação correspondente? Digite R para residência, I para Industria e C para Comércio : ");
consumo = int(input("Qual foi seu consumo em kWh ? "));



if instalacao_tipo == R:
	if consumo <= 500 :
		calc = consumo * 0.40;
		print ("O valor do consumo total de sua Residência foi de %4.2f " %calc);
	elif consumo < 1000:
		calc = consumo * 0.65;
		print ("O valor do consumo total de sua Residência foi de %4.2f " %calc);
elif instalacao_tipo == C:
	if consumo <= 1000;
		calc = consumo * 0.55;
		print ("O valor do consumo total de sua Comercio foi de %4.2f " % calc);
	elif cosumo < 5000:
		calc = consumo * 0.60;
		print ("O valor do consumo total de sua Comercio foi de %4.2f " % calc);
elif instalacao_tipo == I:
	if consumo <= 5000:
		calc = consumo * 0.55;
		print("O valor do consumo total de sua Industria foi de %4.2f" % calc);
	elif consumo > 5000:
		calc = consumo * 0.60;
		print("O valor do consumo total de sua Industria foi de %4.2f" % calc);