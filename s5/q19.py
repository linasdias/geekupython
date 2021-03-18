# inteiro e divisível por 3 ou 5, não pelos dois

num = int(input("Digite um número inteiro e divisivel por 3 ou 5: "))

if((num%3==0) AND (num%5==0)):
    print("Inválido.")
    exit()
else:
    if(num%3==0):
        print("É inteiro e divisível por 3")
        exit()
    elif(num%5==0):
        print("É inteiro e divisível por 5")
        exit()
    else:
        print("Inválido.")
        exit()