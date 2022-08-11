Exercicio 3.10

Faça um programa que calcule o aumento de um salario. Ele deve solicitar o valor do salário e a porgentagem do aumento. Exiba o valor do aumento e do novo salário.


a = int(input("Digite o valor do seu salário : "));
b = float(input("Digite o valor da porcentagem a ser reagustada : "))
c = b*a/100

print("Seu novo salário reajustado fica no valor de R$",c+a,"Com o aumento de ",b,"%");