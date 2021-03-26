num = int(input("Digite um número inteiro maior que 1: "))
if(num<=1):
    print("Inválido!")
    exit()
else:
    i=0
    primo = 0
    for i in range(1, num+1):
        if(num%i==0):
            primo+=1

    if(primo>2):
        print("Não é primo.")
        exit()
    else:
        print("É primo.")
        exit()