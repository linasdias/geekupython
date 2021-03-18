# área do trapézio

bmaior = float(input("Digite a medida da base maior: "))
if bmaior<0:
    print("Valor inválido.")
    exit()
else:
    bmenor = float(input("Digite a medida da base menor: "))
    if bmenor<0:
        print("Valor inválido.")
        exit()
    else:
        altura = float(input("Digite a altura do trapézio: "))
        if altura<0:
            print("Valor inválido.")
            exit()
        else:
            a = ((bmaior+bmenor)*altura)/2
            print("Área: "+str(a))