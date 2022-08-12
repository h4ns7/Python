Exercicio 4.4

Escreva um programa que pergunte o salário do funcionárioe calcule o valor do aumento. Para salários superiores a R$ 1.2500,00, calcule um aumento de 10%. Para os inferiores ou igual, de 15%.




salario = int(input("Digite o valor do seu salário R$ : "))
mult_1 = 0.1
mult_2 = 0.15
if salario >= 1250:
    novo_salario = (salario*mult_1)+ salario;
    print(novo_salario);
else:
    novo_salario = (salario*mult_2)+salario;
    print(novo_salario);
