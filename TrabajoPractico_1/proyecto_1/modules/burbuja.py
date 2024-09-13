def BubbleSort(lista):
    """Ordenamiento que recorre la lista varias veces compara cada par de elementos consecutivos si el primer elemento es mayor que el segundo,
    los intercambia y asi el proceso continúa hasta que no se necesiten más intercambios."""
    for numPasada in range(len(lista)-1,0,-1):
        for i in range(numPasada):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp