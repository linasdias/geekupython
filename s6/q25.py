i=0
soma=0

for i in range(1001):
    if((i%3==0) or (i%5==0)):
        soma+=i
        i+=1
    else:
        i+=1

print("Soma: "+soma)