# imc = peso / (altura^2)

peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso / (altura^2)

if imc <= 18.5:
    print("Abaixo do peso.")
    exit()
elif imc <= 24.9:
    print("Saudável.")
    exit()
elif imc <= 29.9:
    print("Peso em excesso.")
    exit()
elif imc <= 34.9:
    print("Obesidade Grau I")
    exit()
elif imc <= 39.9:
    print("Obesidade Grau II (severa)")
    exit()
elif imc >= 40:
    print("Obesidade Grau III (mórbida)")
    exit()