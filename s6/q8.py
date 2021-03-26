valor = []
cont=0
total=0
while(cont!=10):
    i = int(input("Digite um valor: "))
    valor.append(i)
    cont+=1

print("Maior valor lido: "+max(valor))
print("Menor valor lido: "+min(valor))