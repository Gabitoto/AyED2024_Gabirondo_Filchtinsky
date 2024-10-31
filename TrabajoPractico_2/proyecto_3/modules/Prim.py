from modules.min_heap import monticuloBinario
import sys

def prim(G, inicio):
    cp = monticuloBinario()

    for v in G:
        v.asignar_distancia(sys.maxsize)
        v.asignar_predecesor(None)
    inicio.asignar_distancia(0)
    cp.insertar([(v.obtener_distancia(),v) for v in G])

    while not cp.esta_vacia():
        verticeActual = cp.eliminarMin()
        for verticeSiguiente in verticeActual.obtener_conexiones():
          nuevoCosto = verticeActual.obtener_ponderacion(verticeSiguiente)
          if verticeSiguiente in cp and nuevoCosto < verticeSiguiente.obtener_distancia():
            verticeSiguiente.asignar_predecesor(verticeActual)
            verticeSiguiente.asignar_distancia(nuevoCosto)
            cp.decrementar_clave(verticeSiguiente,nuevoCosto)
