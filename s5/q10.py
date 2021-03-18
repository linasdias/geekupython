# altura

alt = float(input("Digite a altura: "))
sx = input("H ou M?: ")

if(sx=='h' OR sx=='H'):
    ura = (72.7 * alt)-58
elif(sx=='m' OR sx=='M'):
    ura = (62.1 * h)-44.7
else:
    print("Questão inválida.")
    exit()

print("Peso ideal: "+str(ura))
