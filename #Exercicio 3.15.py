#Exercicio 3.15

Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele ja fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos anos de vida um fumante perderá. Exiba o total em dias.


a = int(input("Voce que é fumante ai me responda, quantos cigarros você fuma por dia ? "));
b = int(input("E por quantos anos você tem esse vício ? "));
c = a*10/60;
d = b*360/24;
e = c+d*24;

print("Voce perdeu um total de",e,"dias de vida já");