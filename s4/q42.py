# salário base
sb = float(input("Digite o salário base do funcionário: "))
sb += 0.5*sb
ip = 0.7*sb
sb -= ip
print("Salário a receber: "+str(sb+" reais.")