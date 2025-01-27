class Elemento:
    def __init__(self):
        self.valor = 0
        self.prox = None
    
def busca(chave, primeiro):
    pont = primeiro.prox
    ant = primeiro
    while((pont != None) and (pont.valor < chave)):
        ant = pont
        pont = pont.prox
    return ant,pont

def incluir(chave, primeiro):
    ant,pont = busca(chave,primeiro)
    if ((pont == None) or (pont.valor != chave)):
        novo = Elemento()
        novo.valor = chave
        novo.prox = ant.prox
        ant.prox = novo
    else:
        print("Elemento existe na lista")

def excluir(chave,primeiro):
    ant,pont = busca(chave,primeiro)
    if ((pont != None) and (pont.valor == chave)):
        ptaux = pont
        ant.prox = pont.prox
        del ptaux
    else:
        print("Chave inexistencia")

def mostrar(primeiro):
    pont = primeiro.prox
    while (pont != None):
        print(pont.valor)
        pont = pont.prox
    return

primeiro = Elemento()
primeiro.valor = 0
primeiro.prox = None

cont = 1
while (cont !=0):
    cont = int(input("Digite (1) Inclusão, (2) Exclusão, (3) Mostrar (0)Sair"))
    if (cont==1):
        chave = int(input("Digite valor para incluir"))
        incluir(chave, primeiro)
    elif (cont == 2):
        chave = int(input("Digite valor para excluir"))
        n = excluir(chave, primeiro)
    elif (cont == 3):
        mostrar(primeiro)