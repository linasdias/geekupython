# experiência biológica

print("Digite hora, minuto e segundo do início da experiência quando pedido")
hora = int(input("Hora: "))
minuto = int(input("Minuto: "))
segundo = int(input("Segundo: "))

dura = int(input("Quanto tempo a experiência durou em segundos? "))

segundo += dura 

if(segundo>60)
    inteira = segundo // 60
    minuto += inteira
    segundo = segundo%60

if(minuto>60)
    inteira = minuto // 60
    hora += inteira
    minuto = minuto%60

if(hora>24)
    dia = hora // 24
    hora = hora%24

h = str(hora)
m = str(minuto)
s = str(segundo)
d = str(dia)

print("Durou "+d+" dia(s), "+h+" hora(s), "+m+" minuto(s), e "+s+" segundo(s).")
