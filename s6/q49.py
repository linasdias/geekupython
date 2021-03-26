sal1 = float(input("Digite um salário: "))
sal2 = float(input("Digite outro salário: "))
mes = int(input("Digite o número de meses que a primeira pessoa aplicou: "))

c1 = sal1*0.02*mes
c2 = sal2*0.02
u=0
for u in range(1000):
    if ((c2*u)==c1):
        print("Serão precisos "+str(u)+" meses para que a segunda pessoa alcance a primeira.")