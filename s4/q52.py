# loteria

a1 = float(input("Quanto o amigo 1 apostou? "))
a2 = float(input("Quanto o amigo 2 apostou? "))
a3 = float(input("Quanto o amigo 3 apostou? "))
premio = float(input("Qual o valor do prêmio? "))

apostado = a1+a2+a3
ap1 = a1/apostado
ap2 = a2/apostado
ap3 = a3/apostado

print("Prêmio total: "+premio)
print("Apostador 1: "+str(ap1*100)"%% ou "+str(ap1*premio)+" reais.")
print("Apostador 2: "+str(ap2*100)"%% ou "+str(ap2*premio)+" reais.")
print("Apostador 3: "+str(ap3*100)"%% ou "+str(ap3*premio)+" reais.")