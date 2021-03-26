a = int(input("Digite a: "))
b = int(input("Digite b: "))

i=0
primo=0
soma=0

for i in range(a, b+1):
    for j in range(i+1):
        if(i%j==0):
            primo+=1
            soma+=i
        else:
            primo+=0

print("A soma dos primos entre A e B é "+str(soma))