num = int(input("Digite um número: "))

obs1 = num // 11
obs2 = num // 13
obs3 = num // 17

in1 = num % 11
in2 = num % 13
in3 = num % 17

if(in1==0):
    print("Múltiplo de 11: "+str(obs1+11))
else:
    qq = 11-in1
    print("Múltiplo de 11: "+str(obs1+in1+qq))

if(in2==0):
    print("Múltiplo de 13: "+str(obs2+13))
else:
    qq2 = 13-in2
    print("Múltiplo de 13: "+str(obs2+in2+qq2))

if(in3==0):
    print("Múltiplo de 17: "+str(obs3+17))
else:
    qq3 = 17-in3
    print("Múltiplo de 17: "+str(obs3+in3+qq3))