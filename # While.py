# While

x = int(input("Digite o inicio da tabuada")
y = int(input("Digite o fim da tabuada")

while y <= x :
	print(y+x)
x=x+1


x = int(input("Digite o primeiro numero"))
y = int(input("Digite o segundo numero"))
i = 1
soma = 0
while i <= y:
    print("Estamos somando seu numero")
    i = i + 1
    soma = soma + x
    
print ("o numero somado é : ", soma)

Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.Escreva o total com juros no periodo 


deposito = float(input("Digite o valor R$: "))
juros = float(input("Digite a % de juros ao mês : "))

i = 1
deposito_juros = 0
while i <= 24:
	deposito_juros = deposito_juros + (deposito * juros/100)
	print("valor do juros é : R$ %4.2f" % deposito_juros)
	i = i +1


Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no inicio de cada mês e você deve considera-lo para o caálculo de juros ao mês seguinte.


deposito = float(input("Digite o valor R$: "))
valor_mensal = float(input("Qual valor deseja depositar mensalmente ? "))
juros = float(input("Digite a % de juros ao mês : "))

i = 1
deposito_juros = 0
while i <= 24:
	deposito_juros = deposito_juros + valor_mensal +(deposito * juros/100)
	print("valor do juros é : R$ %4.2f" % deposito_juros)
	i = i +1

#Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte o valor mensal que será pago.Imprima o número de meses para que a dívida seja paga, o total de juros pago.

dívida = float(input("Dívida: "))
taxa = float(input("Juros (Ex.: 3 para 3%): "))
pagamento = float(input("Pagamento mensal:"))
mês = 1
if (dívida * (taxa/100) > pagamento):
    print("Sua dívida não será paga nunca, pois os juros são superiores ao pagamento mensal.")
else:
    saldo = dívida
    juros_pago = 0
    while saldo > pagamento:
        juros = saldo * taxa / 100
        saldo = saldo + juros - pagamento
        juros_pago = juros_pago + juros
        print(f"Saldo da dívida no mês {mês} é de R${saldo:6.2f}.")
        mês = mês + 1
    print(f"Para pagar uma dívida de R${dívida:8.2f}, a {taxa:5.2f} % de juros,")
    print(f"você precisará de {mês - 1} meses, pagando um total de R${juros_pago:8.2f} de juros.")
    print(f"No último mês, você teria um saldo residual de R${saldo:8.2f} a pagar.")





# Escreva um programa que leia números inteiros do teclado. O programa deve ler até que o usuario digite 0.
# no final da execução exiba a quantidade de números digitados, assim como a soma e a média aritimetica


soma = 0
media = 0
i = 1
while i < 1000:
	a = int(input("digite um número inteiro.."))
	if a != 0:
		soma = soma + a
		media = soma/i 
		i = i+ 1
	else: 
		print("Soma",soma)
		print("Media",media)
		print("numero digitados",i)


# Exercicio 5.15 Escreva um programa para controlar uma pequena maquina registradora. Voce deve
# solicitar ao usuario que digite o codigo do produto e a quantidade comprada. Ultilize a tabela
# de codigos abaixo para obter o preço de cada produto.


# seu programa deve exibir o total das compras depois qe o usuario digitar 0.
# Qualquer outro codigo deve gerar a mensagem de erro "Codigo inválido"

apagar = 0
while True:
    código = int(input("Código da mercadoria (0 para sair): "))
    preço = 0
    if código == 0:
        break
    elif código == 1:
        preço = 0.50
    elif código == 2:
        preço = 1.00
    elif código == 3:
        preço = 4.00
    elif código == 5:
        preço = 7.00
    elif código == 9:
        preço = 8.00
    else:
        print("Código inválido!")
    if preço != 0:
        quantidade = int(input("Quantidade: "))
        apagar = apagar + (preço * quantidade)
print(f"Total a pagar R${apagar:8.2f}")






while True:
    print("""

Menu
----
1 - Adição
2 - Subtração
3 - Divisão
4 - Multiplicação
5 - Sair

""")
    opção = int(input("Escolha uma opção:"))
    if opção == 5:
        break
    elif opção >= 1 and opção < 5:
        n = int(input("Tabuada de:"))
        x = 1
        while x <= 10:
            if opção == 1:
                print(f"{n} + {x} = {n + x}")
            elif opção == 2:
                print(f"{n} - {x} = {n - x}")
            elif opção == 3:
                print(f"{n} / {x} = {n / x:5.4f}")
            elif opção == 4:
                print(f"{n} x {x} = {n * x}")
            x = x + 1
    else:
        print("Opção inválida!")