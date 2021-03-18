# logaritmo do positivo
import math

num = int(input("Digite um número inteiro positivo: "))
if num<0:
    print("Inválido")
    exit()
else:
    lg = str(math.log(num))
    print("Logaritmo natural: "+lg)