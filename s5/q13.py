# média ponderada das notas de 3 provas
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

md = (n1*1 + n2*1 + n3*2)/5

print("Média ponderada: "+str(md))
if md > 60:
    print("Aprovado!")
    exit()
else:
    print("Reprovado.")