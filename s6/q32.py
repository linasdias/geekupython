import random

x = random.randint(1,7)
y = random.randint(1,7)

if(x>y):
    print(str(x)+" > "+str(y))
elif(y>x):
    print(str(x)+" < "+str(y))
elif(x==y):
    print(str(x)+" = "+str(y))