n = int(input("Digite um número: "))

def fat(n):
    fat = 1
    j = 2
    while j <= n:
        fat = fat*j
        j = j + 1
    return j

i=0
e=1

for i in range(1, n+1):
    e+= 1/fat(i)

print("E(n) = "+e)