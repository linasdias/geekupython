#empréstimo

sal = float(input("Digite o salário: "))
emp = float(input("Digite o valor do empréstimo: "))

if(emp >= 0.2*sal):
    print("Empréstimo não concedido.")
    exit()
else:
    print("Empréstimo concedido.")