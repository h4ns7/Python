#Exercicio 4.3

Escreva um programa que leia três números e que imprima o maior e o menor.




a = int(input("Digite um número : "));
b = int(input("Digite outro número : "));
c = int(input("Digite denovo um número : "));


if (a < b) and (a < c):
	print ("O menor número digitado é o %2.2d" % (a))
elif (b < a) and (b < c):
	print ("O menor número digitado é o %2.2d" % (b))
elif (c < b) and (c < a):
	print ("O menor número digitado é o %2.2d" % (c))
if (a > b) and (a > c):
	print("Número maior é o primeiro digitado %2.2d" % (a))
elif (b > a) and (b > c):
	print("Número maior é o segundo digitado %2.2d" % (b))
elif (c > a) and (c > b):
	print ("Número maior é o terceiro digitado %2.2d" % (c))