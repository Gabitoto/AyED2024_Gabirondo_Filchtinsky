# módulo para organizar funciones o clases utilizadas en nuestro proyecto

# Actividad numero 1:

# Bubble Sort:

import random as r
 
def BubbleSort(lista):
    for numPasada in range(len(lista)-1,0,-1):
        for i in range(numPasada):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp

lista = [(r.randint(10000,99999)) for _ in range(500)]
ordenamiento = BubbleSort(lista)
print(lista)

# Quick Sort

def ordenamientoRapido(unaLista):
   ordenamientoRapidoAuxiliar(unaLista,0,len(unaLista)-1)

def ordenamientoRapidoAuxiliar(unaLista,primero,ultimo):
   if primero<ultimo:

       puntoDivision = particion(unaLista,primero,ultimo)

       ordenamientoRapidoAuxiliar(unaLista,primero,puntoDivision-1)
       ordenamientoRapidoAuxiliar(unaLista,puntoDivision+1,ultimo)


def particion(unaLista,primero,ultimo):
   valorPivote = unaLista[primero]

   marcaIzq = primero+1
   marcaDer = ultimo

   hecho = False
   while not hecho:

       while marcaIzq <= marcaDer and unaLista[marcaIzq] <= valorPivote:
           marcaIzq = marcaIzq + 1

       while unaLista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
           marcaDer = marcaDer -1

       if marcaDer < marcaIzq:
           hecho = True
       else:
           temp = unaLista[marcaIzq]
           unaLista[marcaIzq] = unaLista[marcaDer]
           unaLista[marcaDer] = temp

   temp = unaLista[primero]
   unaLista[primero] = unaLista[marcaDer]
   unaLista[marcaDer] = temp


   return marcaDer

unaLista = [(r.randint(10000,99999)) for x in range(r.randint(500,1000))]
ordenamientoRapido(unaLista)
print(unaLista)

# Radix Sort

def radix_sort(lista):
    n = 0 
    for e in lista:
        if len(e) > n:
            n = len(e)
    
    for i in range(0, len(lista)):
        while len(lista[i]) < n:
            lista[i] = "0" + lista[i]

    for j in range(n -1, -1, -1):
        grupos = [[] for x in range(10)]
        for i in range(len(lista)):
            grupos[int(lista[i][j])].append(lista[i])
        lista= []
        for g in grupos:
            lista += g
            
    return [int(i) for i in lista]
            
    
lista = [str(r.randint(10000,99999)) for x in range(10)]

