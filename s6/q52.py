saque = float(input("Digite o valor do saque: "))

cem = saque // 100
cinq = (saque%100) // 50
vint = ((saque%100) % 50) // 20
dez = (((saque%100) % 50) % 20) // 10
cinc = ((((saque%100) % 50) % 20) % 10) // 5
dois = (((((saque%100) % 50) % 20) % 10) % 5) // 2
um = (((((saque%100) % 50) % 20) % 10) % 5) % 2

print("Serão precisas:")
print(str(cem)+" nota(s) de 100 reais, ")
print(str(cinq)+" nota(s) de 50 reais, ")
print(str(vint)+" nota(s) de 20 reais, ")
print(str(dez)+" nota(s) de 10 reais, ")
print(str(cinc)+" nota(s) de 5 reais, ")
print(str(dois)+" nota(s) de 2 reais, ")
print(str(um)+" nota(s) de 1 real, ")
