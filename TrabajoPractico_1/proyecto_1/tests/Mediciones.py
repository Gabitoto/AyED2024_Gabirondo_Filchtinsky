# Codigo para medir el rendimiento de los algoritmos de ordenamiento.

import time 
import matplotlib.pyplot as plt
from random import randint as r
from modules.radixSort import radix_sort
from modules.burbuja import BubbleSort
from modules.quickSort import ordenamientoRapido



tamaños = list(range(1, 800))

tiempos_burbuja = []
tiempos_quicksort = []
tiempos_radix = []
tiempos_sorted = []

fig, ax = plt.subplots()

for tamaño in tamaños:
    lista = [r(10000, 99999) for _ in range(tamaño)]
    lista2 = [str(r(10000, 99999)) for _ in range(tamaño)]
    
    inicio = time.time()
    BubbleSort(lista.copy())
    tiempos_burbuja.append(time.time() - inicio)
    
    inicio = time.time()
    ordenamientoRapido(lista.copy())
    tiempos_quicksort.append(time.time() - inicio)
    
    inicio = time.time()
    radix_sort(lista2.copy())
    tiempos_radix.append(time.time() - inicio)
    
    inicio = time.time()
    sorted(lista.copy())
    tiempos_sorted.append(time.time() - inicio)

# Graficar los tiempos de ejecución
ax.plot(tamaños, tiempos_burbuja, label='Burbuja')
ax.plot(tamaños, tiempos_quicksort, label='Quicksort')
ax.plot(tamaños, tiempos_radix, label='Radix Sort')
ax.plot(tamaños, tiempos_sorted, label='funcion Build-in Sorted')
ax.set_xlabel('Tamaño de la lista')
ax.set_ylabel('Tiempo de ejecución (segundos)')
ax.legend()
plt.show()