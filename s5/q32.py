# cardápio

cod = int(input("Digite o código do produto: "))
qtd = int(input("Digite a quantidade: "))

def cq():
    print("O preço é "+str(1.20*qtd))

def bs():
    print("O preço é "+str(1.30*qtd))

def bo():
    print("O preço é "+str(1.50*qtd))

def hb():
    print("O preço é "+str(1.20*qtd))

def cb():
    print("O preço é "+str(1.70*qtd))

def suco():
    print("O preço é "+str(2.20*qtd))

def refri():
    print("O preço é "+str(1.00*qtd))

card = {
    100: cq,
    101: bs,
    102: bo,
    103: hb,
    104: cb,
    105: suco,
    106: refri
}

card.get(cod)()