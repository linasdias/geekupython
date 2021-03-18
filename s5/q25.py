# eq segundo grau
import math

a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

delta = (b^2) - 4*a*c
rz1 = ((-1*b)+math.sqrt(delta))/(2*a)
rz2 = ((-1*b)-math.sqrt(delta))/(2*a)

if(delta<0):
    print("Não existe raiz.")
    exit()
elif(delta==0):
    print("Raiz única.")
    print("Raiz: "+str(rz1))
else:
    print("Duas raízes: "+str(rz1)+" e "+str(rz2))