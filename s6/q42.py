import math

while True:
    v = float(input("Digite um número: "))
    
    if not(v>0):
        exit()

    print("Quadrado: "+str(v^2))
    print("Cubo: "+str(v^3))
    print("Raiz quadrada: "+str(sqrt(v)))

    