import random

a = random.randrange(1, 101)
b = random.randrange(1, 101)

acertos = 0
erros = 0
perguntas = 5

while(perguntas > 0):
    ans = int(input("Qual é a soma de "+str(a)+" + "+str(b)+"? : "))
    cor = a+b
    if(ans == cor):
        print("Correto!")
        acertos+=1
    else:
        print("Incorreto! A resposta era "+str(cor))
        erros+=1
    perguntas-=1

print("Fim da prova!")
print("Acertos: "+str(acertos))
print("Erros: "+str(erros))
