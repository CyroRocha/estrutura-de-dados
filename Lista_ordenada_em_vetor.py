def buscar(chave,n):
    ind = 0
    while((ind<n) and (lista[ind]<chave)):
        ind = ind + 1
    return ind

def buscabinaria(chave, n):
    inf = 0;
    sup = n-1;
    meio = 0;
    while (inf <= sup):
        meio = (inf + sup)//2;
        if (lista[meio]== chave):
            inf = sup + 1
        else:
            if(chave < lista[meio]):
                sup = meio - 1
            else:
                inf = meio + 1;
    if(lista[meio]== chave):
        return
    else:
        return - 1;

def incluir(chave,n,m):
    ind = 0;
    if n < m:
        ind = buscar(chave,n)
        if (ind==n):
            lista[n] = chave
            n = n + 1
        else:
            if (lista[ind] !=chave):
                i = n - 1 
                while i > ind:
                    lista[i+1] = lista[i]
                    i = i- 1
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
        if ((ind <n) and (lista[ind]==chave)):
            for i in range(ind,n):
                lista[i] = lista[i + 1]
            n = n - 1
        else: 
            print("Número não existe na lista.")
    else:
        print("Underflow")
    return n 

lista = [0,0,0,0,0,0,0,0,0,0]
n = 0
m = 10
cont = 1
while (cont !=0):
    cont = int(input("Digite (1) Inclusão,(2) exclusão, (3) mostrar lista, (4) busca binaria, (0) Sair"))
    if (cont == 1):
        chave = int(input("Digite valor para incluir"))
    else:
        if (cont==2):
            chave = int(input("Digite valor para excluir"))
            n = excluir(chave,n)
        else:
            if (cont == 3):
                for i in range(0,n):
                    print(lista[i])
            else:
                if (cont==4):
                    chave = int(input("Digite um valor para buscar"));
                    ind = buscabinaria(chave,n);
                    if (ind != -1):
                        print("Valor da lista")
                    else:
                        print("Valor não encontrado");