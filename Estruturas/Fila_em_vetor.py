def enfileirar(chave):
    global fim
    global inicio
    global num
    global tam
    print(fim)
    if (num <= tam):
        fim = fim + 1
        if (fim > tam):
            fim = 0
        lista[fim] = chave;
        if (inicio == -1):
            inicio = fim;
        num = num + 1
    else:
        print("Overflow")

def desenfileirar():
    global fim
    global inicio
    global tam
    global num
    if (num >0):
        chave = lista[inicio]
        inicio = inicio + 1
        if (inicio > tam):
            inicio = 0
        print(chave);
        num = num - 1
    else:
        print("Underflow")


lista = [0,0,0,0,0,0,0,0,0,0]
inicio = -1
fim = -1
num = 0
tam = 9
cont = 1
print(fim + 1)
while (cont !=0):
    cont = int(input("Digite (1) Enfileirar, (2) Desemfileirar, (0) sair"))
    if (cont == 1):
        chave = int(input("Digite valor para empilhar"))
        enfileirar(chave)
    else:
        if (cont==2):
            desenfileirar();