# aposentadoria

idade = int(input("Digite a idade: "))
tempo = int(input("Quantidade de anos de trabalho: "))

if(idade>=65):
    print("Pode.")
    exit()
else:
    if(tempo>=30):
        print("Pode.")
        exit()
    else:
        if((idade>=60) and (tempo>=25)):
            print("Pode.")
            exit()
        else:
            print("Não pode.")
            exit()