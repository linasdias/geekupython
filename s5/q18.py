# operações matemáticas

print("Menu: ")
print("1. Adição de dois números")
print("2. Subtração de dois números")
print("3. Multiplicação entre dois números")
print("4. Divisão entre dois números")
num = int(input("> Digite o número da operação desejada: "))
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))


def add():
    print(str(n1+n2))

def sub():
    print(str(n1-n2))

def mul():
    print(str(n1*n2))

def div():
    print(str(n1/n2))

cases = {
    1: add,
    2: sub,
    3: mul,
    4: div,
}

cases.get(num)()