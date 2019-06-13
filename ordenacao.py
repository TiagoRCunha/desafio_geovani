#METODO BUBBLE
def bubbleSort(lista):
    tam = len(lista)
    for num in range(0,tam):
        for i in range(0,tam - 1):
            if (lista[i] > lista[i + 1]):
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
    return lista

# METODO SELECTED

def selectionSort(lista):
    tam = len(lista);
    var = 0;
    for i in range(tam):
        sel = lista[i];
        idx = i;
        for j in range(var,tam):
            if (lista[j] < sel):
                sel = lista[j];
                idx = j;
        var += 1;
        aux = lista[i];
        lista[i] = lista[idx];
        lista[idx] = aux;
    return lista

# METODO MERGE
array = [5,4,7,1,6,2,9,3,8];
def mergeSort(lista):

    if len(lista) > 1:

        meio = len(lista)//2

        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]

        mergeSort(listaDaEsquerda), mergeSort(listaDaDireita)

        i = j = k = 0

        while i < len(listaDaEsquerda) and j < len(listaDaDireita):

            if listaDaEsquerda[i] < listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                j += 1
            k += 1

        while i < len(listaDaEsquerda):

            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1

        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1
    return lista