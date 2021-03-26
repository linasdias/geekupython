n = int(input("Digite um número: "))
i=0
h=0
for i in range(1, n+1):
    h+= 1/i

print("H(n) = "+h)