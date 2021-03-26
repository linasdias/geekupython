cont=0
v = []

while True:
    i = int(input("Digite um número inteiro: "))
    v.append(i)
    cont+=1

    if not(i>0):
        break

print("Maior número lido: "+str(max(v)))
print("Menor número lido: "+str(min(v)))