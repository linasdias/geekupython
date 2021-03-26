valor = []
cont=0
total=0
while(cont!=10):
    i = int(input("Digite um valor: "))
    if (i<0):
        print("Inválido!!!")
        exit()
    else:
        valor.append(i)
        total+=i
        cont+=1