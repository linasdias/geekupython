# 780k, primeiro 46%, segundo 32%, terceiro resto

primeiro = 780_000 * 0.46
segundo = 780_000 * 0.32
terceiro = 780_000 - (primeiro+segundo)

print("Primeiro: "+str(primeiro)+" reais.") #358_800 reais
print("Segundo: "+str(segundo)+" reais.") #249_600 reais
print("Terceiro: "+str(terceiro)+" reais.") #171_600 reais