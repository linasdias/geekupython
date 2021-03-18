# mês

m = int(input("Digite um número entre 1 e 12: "))

def jan():
    print("Janeiro")

def fev():
    print("Fevereiro")

def mar():
    print("Março")

def abr():
    print("Abril")

def mai():
    print("Maio")

def jun():
    print("Junho")

def jul():
    print("Julho")

def ago():
    print("Agosto")

def sete():
    print("Setembro")

def out():
    print("Outubro")

def nov():
    print("Novembro")

def dez():
    print("Dezembro")

cases = {
    1: jan,
    2: fev,
    3: mar,
    4: abr,
    5: mai,
    6: jun,
    7: jul,
    8: ago,
    9: sete,
    10: out,
    11: nov,
    12: dez
}

cases.get(m)()