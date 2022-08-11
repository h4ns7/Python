#Exercicio 3.9

Escreva um programa que leia a quatidade de dias, horas, minutos e segundos do usuario. Calcule o total em segundos


a = int(input("Digite a quantidade de dias que queira calcular em segundos : "));
b = int(input("Digite a quantidade de horas que queria calcular em segundos : "));
c = int(input("Digite a quantidade de minutos que queira calcular em segundos : "));
d = a*24*60*60;
e = b*60*60;
f = c*60;
g = d+e+f;


print("A quantidade de segundos contida em tudo é de ",g,"Segundos!");