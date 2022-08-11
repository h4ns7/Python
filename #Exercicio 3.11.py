#Exercicio 3.11

Faça um programa que solicite o preço de uma mercadoria e o pecentual de desconto. Exiba o valor do desconto  e o preço a pagar.


a = float(input("Informe o preço do produto : "));
b = float(input("Informe o total de desconto : "));
c = b*a/100;


print("O valor do produto a ser pago é R$",a-c);