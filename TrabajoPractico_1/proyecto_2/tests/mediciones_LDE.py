# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:02:03 2022

@author: jinsfran

Medición de tiempos de ejecución y graficación
    Escriba un programa que permita medir el tiempo de ejecución de una función que obtiene todas las combinaciones de una lista de n números creados al azar tomando los números de a r valores. El programa debe medir el tiempo de ejecución para los valores de r en el rango de 1 a n.
    Para encontrar las combinaciones, puede utilizar la función “combinations” del módulo “itertools” o crear su propio algoritmo.
    El programa debe crear un gráfico que muestre el tiempo de ejecución versus r. El gráfico debe tener título, leyendas en ambos ejes, una grilla y un marcador que indique el máximo tiempo.
    Indicar, analizando la gráfica el valor de r para el cual el tiempo de ejecución es mayor.
"""
from modules.LDE import ListaDobleEnlazada
import random
import time
import matplotlib.pyplot as plt

n_max = 10000
pasos = 1000

list_sizes = range(1000, n_max + 1, pasos)
tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []

def generar_lista_doble_enlazada(tamaño):
    lista = ListaDobleEnlazada()
    for _ in range(tamaño):
        lista.agregar_al_inicio(random.randint(-10, 10))
    return lista

"""Medir tiempos de ejecución para cada lista"""
for size in list_sizes:
    lista = generar_lista_doble_enlazada(size)
    
    # len()
    start_time = time.perf_counter()
    len(lista)
    end_time = time.perf_counter()
    tiempos_len.append(end_time - start_time)

    # copiar()
    start_time = time.perf_counter()
    lista.copiar()
    end_time = time.perf_counter()
    tiempos_copiar.append(end_time - start_time)

    # invertir()
    start_time = time.perf_counter()
    lista.invertir()
    end_time = time.perf_counter()
    tiempos_invertir.append(end_time - start_time)

"""Graficar los resultados"""
plt.plot(list_sizes, tiempos_len, label='len()')
plt.plot(list_sizes, tiempos_copiar, label='copiar()')
plt.plot(list_sizes, tiempos_invertir, label='invertir()')

"""Etiquetas y título"""
plt.title('N vs Tiempo de Ejecución para Métodos len, copiar e invertir')
plt.xlabel('Cantidad de elementos (N)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.legend()
plt.grid(True)
plt.show()
