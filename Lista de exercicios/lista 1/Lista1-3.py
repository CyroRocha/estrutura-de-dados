#Apresentar os algoritmos de inclusão e exclusão para uma lista ordenada com alocação encadeada, com nó cabeçalho (header).

class Elemento:
    def _init_(self):
        self.valor = 0
        self.prox = None

def busca(chave,primeiro):
    pont = primeiro.prox
    ant = primeiro
    while((pont != None) and pont.valor <chave):
        ant = pont
        pont = pont.prox
    return ant,pont

def incluir(chave, primeiro):
    ant, pont = busca(chave,primeiro)
    if ((pont == None) or (pont.valor != chave)):
        novo = Elemento()
        novo.valor = chave
        novo.prox = ant.prox
        ant.prox = novo
    else:
        print("Elemento já existe na lista")

def excluir(chave,primeiro):
    ant, pont = busca(chave,primeiro)
    if ((pont != None) and (pont.valor == chave)):
        ptaux = pont
        ant.prox = pont.prox
        del ptaux
    else:
        print("Chave inexistente")