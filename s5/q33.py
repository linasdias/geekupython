# aumento de preços

preco = float(input("Digite o preço antigo: "))


if preco < 50:
    preco *= 1.05
elif preco <= 100:
    preco *= 1.1
elif preco > 100:
    preco *= 1.15

if preco < 80:
    print("Barato")
    exit()
elif preco <= 120:
    print("Normal")
    exit()
elif preco <= 200:
    print("Caro")
    exit()
elif preco > 200:
    print("Muito caro")
    exit()