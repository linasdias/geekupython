n = int(input("Digite um número inteiro: "))

for i in range(1, n+1):
    if(i%2!=0):
        print(i)
        i+=1
    else:
        i+=1