# conceito

nota = int(input("Digite a nota do aluno [1-5 para A-E]: "))
falta = int(input("Digite o número de faltas: "))

if falta<20:
    print("O conceito é "+nota)
    exit()
else:
    def a():
        print("O conceito é B")
        exit()

    def b():
        print("O conceito é C")
        exit()

    def c():
        print("O conceito é D")
        exit()

    def d():
        print("O conceito é E")
        exit()

    def e():
        print("O conceito é E")
        exit()

    notas = {
        1: a,
        2: b,
        3: c,
        4: d,
        5: e
    }

    notas.get(nota)()