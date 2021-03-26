num = int(input("Digite um número: "))
if ((num<0) or (num>999)):
    print("Inválido!!!")
    exit()
else:
    if(num<10):
        print(num)
    elif(num<100):
        n1 = str(num // 10)
        n2 = str(num % 10)
        print("U: "+n2+" D: "+n1)
    elif(num<999):
        n1 = str(num // 100)
        
        n2 = num // 10
        if(n2>=10):
            n2 -= (num // 100)*10
            
        n2 = str(n2)

        n3 = str(num % 10)
        print("C: "+n1+" D: "+n2+" U: "+n3)
