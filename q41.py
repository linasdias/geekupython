# valor a ser pago ao funcionário
vdh = float(input("Digite o valor da hora de trabalho em reais: "))
htm = float(input("Digite o número de horas trabalhadas no mês: "))

vp = str((vdh*htm)*1.1)

print("Valor a ser pago ao funcionário: "+vp+" reais.")