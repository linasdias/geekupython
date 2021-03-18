# mais um menu

print("Escolha a opção: ")
print("1 - Soma de 2 números.")
print("2 - Diferença entre 2 números (maior pelo menor).")
print("3 - Produto entre 2 números.")
print("4 - Divisão entre 2 números (o denominador não pode ser zero).")
num = int(input("Opção: "))
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if((num==3) and (n2==0)):
    print("Inválido.")
    exit()
else:

    def soma():
        print(str(n1+n2))

    def dif():
        print(str(n1-n2))

    def prod():
        print(str(n1*n2))

    def div():
        print(str(n1/n2))
    
    op = {
        1: soma,
        2: dif,
        3: prod,
        4: div
    }

    op.get(num)()