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