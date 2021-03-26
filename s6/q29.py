def fat(n):
    fat = 1
    j = 2
    while j <= n:
        fat = fat*j
        j = j + 1
    return j

i=0
s=0

for i in range(6):
    s += i/fat(i*2)

print("S = "+s)