#Exercicio 3.14

Escreva um programa que pergunte a quantidade de km percorridos por u carro alugado pelo usúario, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$0,15 por km rodado.

a = float(input("Quantos KM o S.r ou Sra. ultilizou ? "));
b = int(input("Por quantos dias o veiculo foi alugado ou ultilzado ? "));
c = b*60;
d = a*0.15;


print("o preço total a ser pago é de R$",d+c);