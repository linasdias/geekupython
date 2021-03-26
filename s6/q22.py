print("Digite uma sequência de notas válidas no intervalo de 10 a 20:")
i=0
j=0

while True:
    i = float(input("Digite uma nota: "))
    j+=1
    media+=i

    if not((i<10) or (i>20)):
        print("Valor inválido inserido. Encerrando...")
        media /= j
        print("Média aritmética: "+media)
        exit()