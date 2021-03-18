num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if(num1 > num2): 
    print("O maior é "+str(num1))
elif(num2 > num1): 
    print("O maior é "+str(num2))
else: 
    print("Números iguais.")