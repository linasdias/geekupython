pos = int(input("Digite um número positivo: "))
i=0
soma=0

for i in range(1, pos):
    if(pos%i==0):
        soma+=i
        i+=1
    else:
        i+=1

print("A soma dos divisores do número "+pos+" é "+soma)