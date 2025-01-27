def empilhar(chave,topo,m):
    if topo <m:
        topo = topo + 1
        lista[topo] = chave
    else:
        print("Overflow")
    return topo

def desempilhar(topo):
    chave = 0
    if (topo >-1):
        chave = lista[topo]
        topo = topo -1
        print(chave);
    else:
        print("Underflow")
    return topo

lista = [0,0,0,0,0,0,0,0,0,0]
topo = -1
m = 9
cont = 1
while (cont != 0):
    cont = int(input("Digite (1) Empilhar, (2)Desempilhar, (0)Sair"))
    if (cont==1):
        chave = int(input("Digite valor para empilhar"))
        topo = empilhar(chave, topo, m)
    else:
        if (cont == 2):
            topo = desempilhar(topo)