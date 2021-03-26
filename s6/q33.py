def zero(num):
    if (num==0):
        print("Inválido!")
        exit()

k=0
l=0
lista = []
n = int(input("Digite n: "))
i = int(input("Digite i, diferente de zero: "))
zero(i)
j = int(input("Digite j, diferente de zero: "))
zero(j)

for l in range(1000):
    if(k==n):
        break

    if((l%i==0) or (l%j==0)):
        lista.append(l)
        k+=1

print(lista)