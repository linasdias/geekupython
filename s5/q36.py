# venda mensal

venda = float(input("Digite o valor da venda: "))

if venda < 20_000:
    com = 400 + 0.14*venda
elif venda < 40_000:
    com = 500 + 0.14*venda
elif venda < 60_000:
    com = 550 + 0.14*venda
elif venda < 80_000:
    com = 600 + 0.14*venda
elif venda < 100_000:
    com = 650 + 0.14*venda
elif venda >= 100_000:
    com = 700 + 0.16*venda

print("A comissão a ser paga é de "+str(com))