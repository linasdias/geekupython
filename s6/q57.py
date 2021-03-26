a = int(input("Digite a: "))
b = int(input("Digite b: "))

i=0
primo=0

for i in range(a, b+1):
    for j in range(i+1):
        if(i%j==0):
            primo+=1
        else:
            primo+=0

print("Existe(m) "+str(primo)+" número(s) primo(s) entre A e B.")