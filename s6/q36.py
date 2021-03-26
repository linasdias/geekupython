i=0
sq=0
qs=0

for i in range(101):
    qs+=i
    sq+=(i)^2

qs = (qs)^2

print("Soma dos quadrados: "+str(sq))
print("Quadrado da soma: "+str(qs))

r=0

if(sq>qs):
    r = sq-qs
elif(qs>sq):
    r = qs-sq
elif(sq==qs):
    r = 0

print("Diferença: "+str(r))