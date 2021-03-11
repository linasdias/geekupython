dias = int(input("Digite o número de dias: "))
valor = 30*dias
imposto = valor*0.08

print("Valor a ser pago: "+str(valor-imposto)+" reais, sendo "+str(imposto)+" reais descontados para imposto de renda.")