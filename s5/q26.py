# gasolina

km = float(input("Digite a distância em km: "))
gas = float(input("Digite a quantidade de litros consumidos: "))

consumo = km/gas

if consumo < 8:
    print("Venda o carro!")
elif consumo < 14:
    print("Econômico!")
elif consumo > 12:
    print("Super econômico!")