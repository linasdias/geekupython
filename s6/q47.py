while True:
    print("Menu")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    esc = int(input("Digite uma opção: "))

    if((esc<1) or (esc>5)):
        print("Inválido")
        exit()
    else:
        if not(esc!=5):
            exit()

        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        
        if(esc==1):
            print("Soma = "+str(n1+n2))
        elif(esc==2):
            print("Subtração = "+str(n1-n2))
        elif(esc==3):
            print("Multiplicação = "+str(n1*n2))
        elif(esc==4):
            print("Divisão: "+str(n1/n2))

