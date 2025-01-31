class Elemento:
    def _init_(self):
        self.valor = 0
        self.prox = None
    
def enfileirar(chave,inicio,fim):
    novo= Elemento()
    novo.valor = chave
    novo.prox = None
    if (fim != None):
        fim.prox = novo
    else:
        inicio = novo
    fim = novo
    return inicio, fim

def desenfileirar(inicio, fim):
    if (inicio != None):
        print(inicio.valor)
        ptaux = inicio
        inicio = inicio.prox
        del ptaux
        if (inicio == None):
            fim = None
    else:
        print("Fila vazia")
    return inicio, fim

fim = None
inicio = None

cont = 1
while(cont != 0):
    cont = int(input("Digite (1) Enfileirar, (2) Desenfileirar, (0) sair"))
    if (cont == 1):
        chave = int(input("Digite valor para incluir"))
        inicio, fim = enfileirar(chave, inicio, fim)
    else:
        if (cont == 2):
            if(cont == 2):
                inicio, fim = desenfileirar(inicio,fim)
