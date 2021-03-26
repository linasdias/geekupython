i=0
primo=0
soma=0

for i in range(2_000_000):
    for j in range(1, i+1):
        if(i%j==0):
            primo+=1
            soma+=i

print("Soma: "+str(soma))