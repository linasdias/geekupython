while True:
    r1 = float(input("Digite r1: "))
    
    if not(r1!=0):
        exit()

    r2 = float(input("Digite r2: "))
    r = (r1*r2)/(r1+r2)
    print("R = "+str(r))