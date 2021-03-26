pares = 0
dados = 0
i=0

while True:
    i = int(input("Digite um número: "))
    if(i%2==0):
        print("Par")
        pares+=1
        dados+=1
    else:
        print("Não é par")
        dados+=1
    
    if not (i!=1000):
        break

print("Valores pares: "+str(pares))
print("Valores lidos: "+str(dados))