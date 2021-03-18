# mesmo produto, diferentes estados

valor = float(input("Digite o valor do produto: "))

print("\nEscolha um valor de acordo com o estado:")
print("1. MG")
print("2. SP")
print("3. RJ")
print("4. MS")
c = int(input("Digite um valor: "))
ip = 1

if((c<1) or (c>4)):
    print("Inválido.")
    exit()
else:
    def mg():
        print("Minas Gerais")
        ip += 0.07

    def sp():
        print("São Paulo")
        ip += 0.12

    def rj():
        print("Rio de Janeiro")
        ip += 0.15

    def ms():
        print("Mato Grosso do Sul")
        ip += 0.08

    estado = {
        1: mg,
        2: sp,
        3: rj,
        4: ms
    }

    print("Valor inicial: "+str(valor))
    print("Valor final: "+str(valor*ip))