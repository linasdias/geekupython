pos = int(input("Digite um número positivo: "))
i=0

for i in range(1, pos+1):
    if(pos%i==0):
        print(i)
        i+=1
    else:
        i+=1