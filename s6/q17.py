soma=0
n = int(input("Digite um número inteiro positivo: "))
if(n<0):
    print("Inválido!!!")
    exit()
else:
    for i in range(1, n+1):
        soma+=i