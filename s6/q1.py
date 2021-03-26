cont = 0

for num in range(1,100):
    while(cont!=5):
        if(num%3==0):
            print(num)
            cont+=1
            num+=1
        else: 
            num+=1