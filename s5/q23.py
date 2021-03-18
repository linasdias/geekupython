# ano bissexto

ano = int(input("Digite um ano: "))

if(ano%400==00):
    print("Bissexto")
    exit()
elif((ano%4==0) and (ano%100!=0)):
    print("Bissexto")
    exit()
else:
    print("Não bissexto.")
    exit()