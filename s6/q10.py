pares=0

for i in range(1,101):
    if(i%2==0):
        pares+=i
        i+=1
    else:
        i+=1

print(pares)