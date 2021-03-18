# raiz
import math

num = int(input("Digite um número inteiro positivo: "))
if(num<0):
    print("Número inválido. Tente novamente.")
    exit()
else: 
    raiz = math.sqrt(num)
    print("A raiz de "+str(num)+" é: "+str(raiz))