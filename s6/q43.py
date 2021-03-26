md=0
vl=0

while True:
    v = float(input("Digite um número: "))
    md+=1
    vl+=v
    
    if not(v!=0):
        break

media = vl/md

print("Média: "+str(media))