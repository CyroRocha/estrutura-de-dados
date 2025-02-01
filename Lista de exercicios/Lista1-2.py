#. Apresentar os algoritmos para busca ordenada e para busca binária, para a lista descrita no exercício 1
#

def buscar (chave,n):
    ind = 0
    while((ind < n) and (lista[ind]<chave)):
        ind = ind + 1
    return ind

def buscabinaria(chave,n):
    inf = 0
    sup = n - 1
    meio = 0
    while (inf <= sup):
        meio = (inf + sup)//2
        if(lista[meio]==chave):
            inf = sup + 1
        else:
            if (chave < lista[meio]):
                sup = meio - 1
            else:
                inf = meio + 1
    if(lista[meio] == chave):
        return meio
    else:
        return -1



lista = [0,0,0,0,0,0,0,0,0,0,0]
n = 0
m = 10
