class Elemento:
    def __init__(self):
        self.valor = 0
        self.prox = None
        self.ant = None

def busca(chave,primeiro):
    ultimo = primeiro.ant
    