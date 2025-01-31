class Elemento:
    def __init__(self):
        self.valor = 0
        self.prox = None

def empilhar(chave, topo):
    novo = Elemento()
    novo.valor = chave
    novo.prox = topo
    topo = novo
    return topo

def desempilhar(topo):
    if (topo != None):
        ptaux = topo
        topo = topo.prox
        del ptaux
    else:
        print("Pilha vazia")
    return topo

topo = None

cont = 1
while (cont != 0):
    cont = int(input("Digite (1) Empilhar, (2) Desempilhar, (0)sair"))
    if (cont == 1):
        chave = int(input("Digite valor para incluir"))
        topo = empilhar(chave, topo)
    else:
        if (cont == 2):
            topo = desempilhar(topo)