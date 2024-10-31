from modules.min_heap import monticuloBinario
import sys

def prim(G, inicio):
    cp = monticuloBinario()
    arbol_expansion = set()  # Para mantener registro de las aristas del árbol
    flujo_mensajes = []  # Lista para almacenar el flujo de mensajes
    visitados = set()  # Conjunto para evitar duplicados
    aldeas_recorridas = set()  # Conjunto para almacenar aldeas recorridas

    # Inicializar todos los vértices
    for v in G:
        v.asignar_distancia(sys.maxsize)
        v.asignar_predecesor(None)
    inicio.asignar_distancia(0)
    
    # Construir el montículo con todos los vértices
    cp.construir_monticulo([(v.obtener_distancia(), v) for v in G])

    while not cp.esta_vacia():
        verticeActual = cp.eliminarMin()
        
        # Solo procesar si no ha sido visitado
        if verticeActual.obtener_id() not in visitados:
            visitados.add(verticeActual.obtener_id())
            aldeas_recorridas.add(verticeActual.obtener_id())
            
            # Si tiene predecesor, registrar el flujo de mensajes
            if verticeActual.obtener_predecesor():
                flujo_mensajes.append({
                    'emisor': verticeActual.obtener_predecesor().obtener_id(),
                    'receptor': verticeActual.obtener_id(),
                    'distancia': verticeActual.obtener_ponderacion(verticeActual.obtener_predecesor())
                })
            
        # Si el vértice tiene predecesor, agregar la arista al árbol
        if verticeActual.obtener_predecesor():
            arbol_expansion.add((verticeActual.obtener_predecesor(), verticeActual))
            
        for verticeSiguiente in verticeActual.obtener_conexiones():
            # Solo procesar vértices no visitados
            if verticeSiguiente not in visitados:
                ponderacion = verticeActual.obtener_ponderacion(verticeSiguiente)
                if verticeSiguiente in cp and ponderacion < verticeSiguiente.obtener_distancia():
                    verticeSiguiente.asignar_predecesor(verticeActual)
                    verticeSiguiente.asignar_distancia(ponderacion)
                    cp.decrementar_clave(verticeSiguiente, ponderacion)

    return  flujo_mensajes, aldeas_recorridas