from modules.Grafo import Grafo
from modules.Prim import prim as p

def cargar_grafo(nombre_archivo):
    grafo = Grafo()
    with open(nombre_archivo, 'r') as file:
        for linea in file:
            partes = linea.split()
            aldea_de = partes[0]
            aldea_a = partes[1]
            ponderacion = int(partes[2])
            grafo.agregar_arista(aldea_de, aldea_a, ponderacion)
    return grafo

def main():
    nombre_archivo = 'data/aldeas.txt'
    grafo = cargar_grafo(nombre_archivo)

    # Supongamos que "Peligros" es la aldea de inicio
    aldea_inicio = grafo.obtener_vertice('Peligros')
    if aldea_inicio is None:
        print("La aldea de inicio 'Peligros' no se encuentra en el grafo.")
        return

    # Ejecutar Prim para encontrar el árbol de expansión mínima
    p(grafo, aldea_inicio)

    # Mostrar los resultados
    print("Árbol de expansión mínima desde la aldea 'Peligros':")
    for vertice in grafo:
        if vertice.obtener_predecesor() is not None:
            print(f"{vertice.obtener_predecesor().obtener_id()} -> {vertice.obtener_id()} (Peso: {vertice.obtener_ponderacion(vertice.obtener_predecesor()):d})")

if __name__ == "__main__":
    main()
