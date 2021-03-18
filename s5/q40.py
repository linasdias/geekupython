# carro novo

cfab = float(input("Digite o custo de fábrica: "))

if cfab < 12_000:
    dis = 0.05*cfab
    imp = 0
elif cfab < 25_000:
    dis = 0.10*cfab
    imp = 0.15*cfab
elif cfab > 25_000:
    dis = 0.15*cfab
    imp = 0.20*cfab

print("Custo ao consumidor: "+str(cfab+dis+imp))