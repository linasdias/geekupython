while True:
    print("Menu")
    print("1. Converter km/h para m/s")
    print("2. Converter m/s para km/h")
    print("3. Sair")
    esc = int(input("Digite a opção escolhida: "))
    
    if((esc<1) or (esc>3)):
        print("Opção inválida")
        exit()
    else:
        if(esc==1):
            kmh = float(input("Digite km/h: "))
            ms = kmh/3.6
            print("Resultado: "+str(ms))
        elif(esc==2):
            ms = float(input("Digite m/s: "))
            kmh = ms*3.6
            print("Resultado: "+str(kmh))

    if not(esc!=3):
        exit()