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

lista = [(r.randint(0,500)) for _ in range(500)]
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

unaLista = [54,26,93,17,77,31,44,55,20]
ordenamientoRapido(unaLista)
print(unaLista)

# Radix Sort



