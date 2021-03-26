n = int(input("Digite um inteiro não negativo: "))
if(n<0):
    print("Inválido")
    exit()
else:
    i=0
    soma=0
    primo=0

    for i in range(n+1):
        
        for j in range(1, i+1):
            if(i%j==0):
                primo+=1

        if(primo>2):
            soma+=0
        else:
            soma+=i

    print("Soma: "+str(soma))