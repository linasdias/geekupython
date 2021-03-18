#inteiro maior que zero, soma dos algarismos

num = input("Digite um número inteiro positivo: ")
if int(num) > 0:
    i = 0
    s = 0
    while i < len(num):
        s = s + int(num[i])
        i = i + 1
    print("A soma dos números é: "+str(s))
else:
    print("Número inválido.")