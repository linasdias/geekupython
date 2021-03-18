#maior e diferença
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

if(num1 > num2):
    dif = str(num1-num2)
    print("O maior é "+str(num1)+", e a diferença é de "+dif)
elif(num2 > num1):
    dif = str(num2-num1)
    print("O maior é "+str(num2)+", e a diferença é de "+dif)
else:
    print("Os dois números são iguais e não há diferença.")