

valor = float(input("Qual valor da casa a ser comprada ? "));
salario = float(input("Qual o seu salário por favor em R$ ? "));
ano = int(input("Quantidade de anos a pagar : "));



mes_ = (ano * 12);
valor_mes = (valor/mes_);
recebo = salario * 0.3;

if valor_mes < recebo:
	print(" Parabens !! seu credito foi aprovado. O valor mensal a ser pago é de : R$%4.2f" %valor_mes);
else: 
	print("O valor da prestação ultrapassa os 30%, por favor ganhe mais !!");
	













