n = int(input("Digite um número inteiro positivo ímpar: "))
if(n%2==0):
    print("Inválido!!!")
    exit()
else:
    if(n<0):
        print("Inválido")
        exit()
    else:
        for i in range(n):
            if(i%2!=0):
                print(i)
                i+=1
            else:
                i+=1