# data válida

dia = int(input("Digite um dia: "))

if ((dia < 0) or (dia > 31)):
    print("Inválido.")
    exit()

mes = int(input("Digite um mês [1-12]: "))

if ((mes < 0) or (mes > 12)):
    print("Inválido.")
    exit()

ano = int(input("Digite um ano [AAAA]: "))

if ((ano < 0) or (ano>2021)):
    print("Inválido.")
    exit()

if mes == 2:
    if ((ano%400==0) or ((ano%4==0)and(ano%100!=0))): #bissexto
        if dia > 29:
            print("Inválido.")
            exit()
    else:
        if dia > 28:
            print("Inválido")
            exit()
else:
    # if mes == jan, mar, mai, jul, ago, out, dez -- 31 dias
    # else -- 30 dias
    if ((((((((mes == 1)or(mes == 3))or(mes == 5))or(mes == 7))or(mes == 8))or(mes == 10))or(mes == 12))):
        if dia > 31:
            print("Inválido.")
            exit()
    else:
        if dia > 30:
            print("Inválido.")
            exit()


print("Data válida!")