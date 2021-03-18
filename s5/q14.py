# nota final
n1 = float(input("Digite a primeira nota: "))

if (n1<0 OR n1>10):
    print("Nota inválida")
    exit()
else:
    n2 = float(input("Digite a segunda nota: "))

    if(n2<0 OR n2>10):
        print("Nota inválida")
        exit()
    else:
        n3 = float(input("Digite a terceira nota: "))

        if(n3<0 OR n3>10):
            print("Nota inválida")
            exit()
        else:
            md = (n1*2 + n2*3 + n3*5)/10
            print("Média: "+str(md))
            if md>2.9:
                print("Reprovado")
            elif md>4.9:
                print("Em recuperação")
            else:
                print("Aprovado!")
