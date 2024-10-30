from modules.cola_prioridad import colaPrioridad
from modules.Vertice import Vertice as v
import sys

def prim(G, inicio):
    cp = colaPrioridad()

    for v in G:
        v.asignar_distancia(sys.maxsize)
        v.asignar_predecesor(None)
    inicio.asignar_distancia(0)
    cp.insertar([(v.obtener_distancia(),v) for v in G])

    while not cp.cola_prioridad.esta_vacia():
        verticeActual = cp.extraer_mayor_prioridad()
        for verticeSiguiente in verticeActual.obtener_conexiones():
          nuevoCosto = verticeActual.obtener_ponderacion(verticeSiguiente)
          if verticeSiguiente in cp and nuevoCosto < verticeSiguiente.obtener_distancia():
            verticeSiguiente.asignar_predecesor(verticeActual)
            verticeSiguiente.asignar_distancia(nuevoCosto)
            cp.decrementar_clave(verticeSiguiente,nuevoCosto)
