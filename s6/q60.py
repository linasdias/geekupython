soma=0
somapares=0
qtd=0
qtdpares=0
nm = []

while True:
    num = int(input("Digite um número:"))
    nm.append(num)
    soma+=num
    qtd+=1

    if(num%2==0):
        somapares+=1
        qtdpares+=1

    if not(num!=0):
        break

md = str(soma/qtd)
maior = str(max(nm))
menor = str(min(nm))
mpares = str(somapares/qtdpares)

print("Menu")
print("1. Soma")
print("2. Quantidade de números digitados")
print("3. Média dos digitados")
print("4. Maior número digitado")
print("5. Menor número digitado")
print("6. Média dos números pares")
print("0. Sair")
esc = int(input("Digite um número: "))

if(esc==0):
    exit()
else:
    if(esc==1):
        print("Soma dos números digitados: "+str(soma))
    elif(esc==2):
        print("Quantidade de números digitados: "+str(qtd))
    elif(esc==3):
        print("Média dos números digitados: "+md)
    elif(esc==4):
        print("Maior número digitado: "+maior)
    elif(esc==5):
        print("Menor número digitado: "+menor)
    elif(esc==6):
        print("Média dos números pares: "+mpares)
