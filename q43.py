# programa de ajuda para vendedores
valor = float(input("Digite um valor: "))
p1 = valor -= valor*0.1
p2 = str(valor/3)
p3 = str(0.5*p1)
p4 = str(0.5*valor)

print("Total a pagar com desconto de 10%: "+str(p1))
print("Valor de cada parcela em 3x sem juros: "+p2)
print("Comissão do vendedor na venda à vista: "+p3)
print("Comissão do vendedor na venda parcelada: "+p4)