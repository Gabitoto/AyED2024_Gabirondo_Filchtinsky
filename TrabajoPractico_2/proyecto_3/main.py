from modules.Grafo import Grafo
from modules.Prim import prim as p

def main():
    with open("aldeas.txt", "r") as archivo:
        grafo = Grafo()
        for linea in archivo:
                partes = linea.strip().split(", ")  # Divide usando coma y espacio
                if len(partes) == 3:  # Verifica que haya exactamente 3 partes
                    aldea_de = partes[0]
                    aldea_a = partes[1]
                    try:
                        ponderacion = int(partes[2])
                        grafo.agregar_arista(aldea_de, aldea_a, ponderacion)
                    except ValueError:
                        print(f"Error de conversión en la línea: {linea.strip()}")
                else:
                    print(f"Formato incorrecto en la línea: {linea.strip()}")

    # Supongamos que "Peligros" es la aldea de inicio
    aldea_inicio = grafo.obtener_vertice('Peligros')
    if aldea_inicio is None:
        print("La aldea de inicio 'Peligros' no se encuentra en el grafo.")
        return
    
    grafo.mostrar_grafo()

    """# Ejecutar Prim para encontrar el árbol de expansión mínima
    p(grafo, aldea_inicio)

    # Mostrar los resultados
    print("Árbol de expansión mínima desde la aldea 'Peligros':")
    for vertice in grafo:
        if vertice.obtener_predecesor() is not None:
            print(f"{vertice.obtener_predecesor().obtener_id()} -> {vertice.obtener_id()} (Peso: {vertice.obtener_ponderacion(vertice.obtener_predecesor()):d})")"""

if __name__ == "__main__":
    main()
