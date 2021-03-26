num = int(input("Ler quantas vezes? "))

valor = []
cont=0
total=0
while(cont!=num):
    i = int(input("Digite um valor: "))
    valor.append(i)
    cont+=1

print("Maior valor lido: "+max(valor))
print("Menor valor lido: "+min(valor))