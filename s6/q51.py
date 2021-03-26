sal = 2000 + (2000*0.015)
i=1997

for i in range(1997, 2021):
    sal*=2
    i+=1
    
    if(i==2021): 
        break

print("Salário atual: "+str(sal))