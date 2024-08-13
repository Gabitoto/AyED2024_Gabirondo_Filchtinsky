# Archivo donde agregare codigo que voy probando de la teoria y investigacion del tema a estudiar.

# Bubble sort

def BubbleSort(lista):
    for numPasada in range(len(lista)-1,0,-1):
        for i in range(numPasada):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp

lista = [54,26,93,17,77,31,44,55,20]
ordenamiento = BubbleSort(lista)
print(lista)


# Bubble Sort Corto

def ordenamientoBurbujaCorto(unaLista):
    intercambios = True
    numPasada = len(unaLista)-1
    while numPasada > 0 and intercambios:
       intercambios = False
       for i in range(numPasada):
           if unaLista[i]>unaLista[i+1]:
               intercambios = True
               temp = unaLista[i]
               unaLista[i] = unaLista[i+1]
               unaLista[i+1] = temp
       numPasada = numPasada-1

unaLista=[20,30,40,90,50,60,70,80,100,110]
ordenamientoBurbujaCorto(unaLista)
print(unaLista)
