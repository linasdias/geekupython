valor = []
cont=0
total=0
while(cont!=10):
    i = int(input("Digite um valor: "))
    valor.append(i)
    total+=i
    cont+=1

media = total/10
print(media)