n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

soma=0
mult=1

for i in range(n1, n2+1):
    if(i%2==0):
        soma+=i
    else:
        mult*=i

print("Soma dos pares: "+soma)
print("Multiplicação dos ímpares: "+mult)