"""Sejam duas listas ordenadas, encadeadas, com nó cabeça. Apresente um algoritmo
que intercale as duas listas, gerando uma terceira lista que inicialmente estará vazia,
de forma que a lista resultante seja também ordenada"""

class Elemento:
    def __init__(self, valor = 0):
        self.valor = valor
        self.prox = None

def Intercalar_lista(lista1,lista2):
    resultado = Elemento()
    atual = resultado

    p1 = lista1.prox
    p2 = lista2.prox

    while ((p1 != None) and p2 != None):
        if p1.valor <= p2.valor :
            atual.prox = Elemento(p1.valor)
            p1 = p1.prox
        else:
            atual.prox = Elemento(p2.valor)
            p2 = p2.prox
        atual = atual.prox

    while (p1 != None):
        atual.prox = Elemento(p1.valor)
        p1 = p1.prox
        atual = atual.prox

    while (p2 != None):
        atual.prox = Elemento(p2.valor)
        p2 = p2.prox
        atual = atual.prox
    return resultado


def mostrar_lista(primeiro):
    pont = primeiro.prox
    while (pont != None):
        print(pont.valor, end="->")
        pont = pont.prox
    print("None")

if __name__ == "__main__":
    lista1 = Elemento()
    lista1.prox = Elemento(1)
    lista1.prox.prox = Elemento(3)
    lista1.prox.prox.prox = Elemento(5)

    lista2 = Elemento()
    lista2.prox = Elemento(2)
    lista2.prox.prox = Elemento(4)
    lista2.prox.prox.prox = Elemento(6)

    print(f'lista 1:')
    mostrar_lista(lista1)

    print(f'Lista 2:')
    mostrar_lista(lista2)

    lista_resultante = Intercalar_lista(lista1, lista2)
    print("lista_resultante :")
    mostrar_lista(lista_resultante)
