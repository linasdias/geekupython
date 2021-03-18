# estacionamento

h1, m1 = int(input("Digite a hora e minuto de chegada: ").split(" "))
h2, m2 = int(input("Digite a hora e minuto de saída: ").split(" "))

if h1 > h2: #dias diferentes
    h2 += 24


total = ((h2-h1)*60 + (m2-m1))/60
if total <= 1:
    print("R$ 1")
elif total <= 2:
    print("R$ 2")
elif total <= 3:
    print("R$ 3.40")
elif total <= 4:
    print("R$ 4.80")
elif total >= 5:
    t = 4.80 + (total - 5)*2