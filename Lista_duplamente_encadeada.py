class Elemento:
    def __init__(self):
        self.valor = 0
        self.prox = None
        self.ant = None

def busca(chave,primeiro):
    ultimo = primeiro.ant
    if ((ultimo != None) and (chave <= ultimo.valor)):
        pont = primeiro.prox
        while (pont.valor < chave):
            pont = pont.prox
            return pont
    else:
        return primeiro

def incluir(chave,primeiro):
    pont = busca(chave, primeiro)
    if((pont == primeiro) or (chave != pont.valor)):
        anterior = pont.ant
        novo = Elemento()
        novo.valor = chave
        novo.prox = pont
        novo.ant = anterior
        anterior.prox = novo
        pont.ant = novo
    else:
        print("Elemento existe na lista")

def excluir(chave,primeiro):
    pont = busca(chave,primeiro)
    if((pont != primeiro) and (pont.valor == chave)):
        anterior = pont.ant 
        proximo = pont.prox
        anterior.prox = proximo
        proximo.ant = anterior
        del pont
    else:
        print("Chave inexistente")

primeiro = Elemento()
primeiro.valor = 0
primeiro.prox = primeiro
primeiro.ant = primeiro

cont = 1
while (cont != 0):
    cont = int(input("Digite (1) Inclusão, (2) Exclusão, (3) mostrar lista, (0)sair "))
    if (cont == 1):
        chave = int(input("Digite valor para incluir"))
        incluir(chave, primeiro)
    else:
        if (cont == 2):
            chave = int(input("Digite valor para excluir"))
            excluir(chave,primeiro)
        else:
            if (cont == 3):
                pont = primeiro.prox
                while (pont != primeiro):
                    print(pont.valor)
                    pont = pont.prox