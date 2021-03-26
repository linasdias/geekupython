inicio = int(input("Digite o valor inicial: "))
final = int(input("Digite o valor final: "))

if(final<inicio):
    print("Inválido!")
    exit()
else:
    i=0
    soma=0
    for i in range(inicio, final+1):
        if(i%2!=0):
            soma+=i
        else:
            soma+=0

    print("Soma dos ímpares neste intervalo: "+str(soma))
