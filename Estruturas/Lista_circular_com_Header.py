class Elemento:
    def __init__(self):
        self.valor = 0
        self.prox = None

class Ponteiros:
    def __init__(self):
        self.ant = None
        self.prox = None


def busca(chave):
    global primeiro
    ponteiros = Ponteiros()
    ponteiros.pont = primeiro.prox
    ponteiros.ant = primeiro
    while ((ponteiros.pont.valor != 0) and (ponteiros.pont.valor <chave)):
        ponteiros.ant = ponteiros.pont
        ponteiros.pont = ponteiros.pont.prox
    return ponteiros

def incluir(chave):
    ponteiros = busca(chave)
    if (ponteiros.pont.valor != chave):
        novo = Elemento()
        novo.valor = chave
        novo.prox = ponteiros.pont
        ponteiros.ant.prox = novo
    else:
        print("Elemento existe na lista")

def excluir(chave):
    ponteiros = busca(chave)
    if (ponteiros.pont.valor == chave):
        ptaux = ponteiros.pont
        ponteiros.ant.prox = ponteiros.pont.prox
        del ptaux
    else:
        print("Chave inexistente")

def mostrar():
    global primeiro
    ptr = Ponteiros()
    ptr.pont = primeiro.prox
    while (ptr.pont.valor !=0):
        print(ptr.pont.valor)
        ptr.pont = ptr.pont.prox
    return

primeiro = Elemento()
primeiro.valor = 0
primeiro.prox = primeiro

cont = 1
while (cont != 0):
    cont = int(input("Digite (1) inclusão, (2) exclusão, (3)mostrar (0 sair)"))
    if (cont==1):
        chave = int(input("Digite valor para incluir"))
        incluir(chave)
    elif (cont == 2):
        chave = int(input("Digite valor para excluir"))
        n = excluir(chave)
    elif (cont == 3):
        mostrar()