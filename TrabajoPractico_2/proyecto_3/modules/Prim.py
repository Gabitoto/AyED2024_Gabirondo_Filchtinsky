from modules.min_heap import monticuloBinario
import sys

def prim(G, inicio):
    cp = monticuloBinario()
    arbol_expansion = set()  # Para mantener registro de las aristas del árbol

    # Inicializar todos los vértices
    for v in G:
        v.asignar_distancia(sys.maxsize)
        v.asignar_predecesor(None)
    inicio.asignar_distancia(0)
    
    # Construir el montículo con todos los vértices
    cp.construir_monticulo([(v.obtener_distancia(), v) for v in G])

    while not cp.esta_vacia():
        verticeActual = cp.eliminarMin()
        
        # Si el vértice tiene predecesor, agregar la arista al árbol
        if verticeActual.obtener_predecesor():
            arbol_expansion.add((verticeActual.obtener_predecesor(), verticeActual))

        for verticeSiguiente in verticeActual.obtener_conexiones():
            ponderacion = verticeActual.obtener_ponderacion(verticeSiguiente)
            if verticeSiguiente in cp and ponderacion < verticeSiguiente.obtener_distancia():
                verticeSiguiente.asignar_predecesor(verticeActual)
                verticeSiguiente.asignar_distancia(ponderacion)
                cp.decrementar_clave(verticeSiguiente, ponderacion)

    return arbol_expansion
