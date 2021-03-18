# real
import math

num = float(input("Digite um número real: "))

if(num<0): #negativo
    num *= num
    print("Ao quadrado: "+str(num))
    exit()
else: #positivo
    raiz = math.sqrt(num)
    print("A raiz de "+str(num)+" é: "+str(raiz))
    exit()