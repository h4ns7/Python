#Exercicio 4.8

Escreva um programa que leia dois números e que pergunte qual operação voce deseja realizar. Voce deve poder calcular a soma (+), subtração(-), multiplicação(*) e divisão(/). Exiba o resultado da operação na tela.




a = float(input("Digite seu primeiro valor : "));
b = float(input("Digite seu segundo valor : "));
c = input("Agora me fale com simbolos Ex: *,/,+,^,- que tipo de operação deseja fazer......");

if c == *:
	mult = a * b;
	print("A multipicação é %4.2f" %mult);
elif c == / :
	div = a / b;
	print("A Divisão é %4.2f" %div);
elif c == +;
	soma = a + b;
	print("A soma é %4.2f" %soma);
elif c == -;
	sub = a - b;
	print("A subtração é %4.2" %sub);
else:
	print("Infelizmente o carater que voce digitou ainda não temos suporte para atender.... mas não se preocupe nossa equipe está trabalhando nisso");