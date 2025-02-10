#Apresentar os algoritmos de inclusão e exclusão em uma lista ordenada com alocação sequencial (em vetor)

def buscar(chave,n):
    ind = 0
    while ((ind < n) and (lista[ind]<chave)):
        ind = ind + 1
    return ind


def incluir(chave,n,m):
    ind = 0
    if n < m:
        ind = buscar(chave,n)
        if (ind == n):
            lista[n] = chave
            n = n + 1
        else:
            if (lista[ind] !=chave):
                i = n - 1
                while i >= ind:
                    lista[i+1] = lista[i]
                    i = i - 1
                lista[ind] = chave
                n = n + 1
            else:
                print("Número não existe na lista.")
    else:
        print("Overflow")
    return n

def excluir(chave,n):
    ind = 0
    i = 0
    if (n>0):
        ind = buscar(chave,n)
        if ((ind < n) and lista[ind]==chave):
            for i in range(ind,n):
                lista[i] = lista[i + 1]
            n = n -1
        else: print("Número não existe na lista. ")
    else:
        print("Underflow")
    return n

lista = [0,0,0,0,0,0,0,0,0,0]