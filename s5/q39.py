# aumento

sal = float(input("Digite o salário: "))
tem = int(input("Digite o tempo de serviço em anos: "))

if sal < 500:
    sal *= 1.25
    print("Sem bônus")
elif sal < 1000:
    sal*= 1.2
    if((tem>=1) and (tem<3)):
        sal+=100
    else:
        print("Sem reajuste.")
elif sal < 1500:
    sal*= 1.15
    if((tem>=4) and (tem<6)):
        sal+=200
    else:
        print("Sem reajuste.")
elif sal < 2000:
    sal*=1.10
    if ((tem>=7) and (tem<10)):
        sal+=300
    else:
        print("Sem reajuste.")
elif sal >= 2000:
    if tem > 10:
        sal+=500
    else:
        print("Sem reajuste.")

print("Salário final reajustado: "+str(sal))