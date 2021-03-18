#switch

d = int(input("Digite um número entre 1 e 7: "))

def dom():
    print("Domingo")

def seg():
    print("Segunda")

def ter():
    print("Terça")

def qua():
    print("Quarta")

def qui():
    print("Quinta")

def sex():
    print("Sexta")

def sab():
    print("Sábado")

cases = {
    1: dom,
    2: seg,
    3: ter,
    4: qua,
    5: qui,
    6: sex,
    7: sab
}

cases.get(d)()