import random
tent = 0

a = random.randrange(1, 1001)

while True:
    b = int(input("Digite sua aposta: "))
    tent+=1

    if not(b!=a):
        print("Parabéns, você acertou depois de "+str(tent)+" tentativas!")