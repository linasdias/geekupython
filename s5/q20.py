# eu sou um triângulo???

a = float(input("Digite a medida do lado A: "))
b = float(input("Digite a medida do lado B: "))
c = float(input("Digite a medida do lado C: "))

if(a<(b+c)):
    if(b<(a+c)):
        if(c<(a+b)):
            if(a==b):
                if(b==c):
                    print("Equilátero.")
                elif(a==c):
                    print("Isósceles.")
                else:
                    print("Isósceles.")
                    if((a!=b) and (a!=c)):
                        print("Escaleno.")
            else:
                print("Não é equilátero.")
        else:
            print("Inválido.")
            exit()
    else:
        print("Inválido.")
        exit()
else:
    print("Inválido.")
    exit()
