# 2 notas

n1 = float(input("Digite a primeira nota: "))
if(n1<0.0 OR n1>10.0):
    print("Nota inválida. Tente novamente.")
    exit()
else:
    n2 = float(input("Digite a segunda nota: "))
    if(n2<0.0 OR n2>10.0):
        print("Nota inválida. Tente novamente.")
        exit()
    else:
        md = str((n1+n2)/2)
        print("Média: "+md)