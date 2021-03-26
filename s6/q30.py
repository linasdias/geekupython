n = int(input("Digite um valor: "))

i = 0
j = 0
k = 0
soma=0

for i in range(n+1):
    soma+=i

print("Sequência 1: "+soma)
soma=0
p = 1

for j in range(2*n):
    if(p%2!=0):
        soma+=j
    else:
        soma-=j

print("Sequência 2: "+soma)
soma=1
p=1

for k in range(2*n):
    if(p%2!=0):
        soma+=k
    else:
        soma+=0 

print("Sequência 3: "+soma)