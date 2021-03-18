# médias
import math

print("Menu")
print("1. Média geométrica")
print("2. Média ponderada")
print("3. Média harmônica")
print("4. Média aritmética")
esc = int(input("Escolha uma opção: "))

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

def mgeo():
    res1 = (a*b*c) ** (1/3)
    print("Resultado: "+str(res1))

def mpon():
    res2 = (a + 2*b + 3*c)/6
    print("Resultado: "+str(res2))

def mhar():
    res3 = 1/(1/a + 1/b + 1/c)
    print("Resultado: "+str(res3))

def mari():
    res4 = (a+b+c)/3
    print("Resultado: "+str(res4))


sw = {
    1: mgeo,
    2: mpon,
    3: mhar,
    4: mari
}

sw.get(esc)()