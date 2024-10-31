from modules.Grafo import Grafo
from modules.Prim import prim as p

def main():
    # Lee las aldeas del archivo
    lista_aldeas = set()
    with open("aldeas.txt", "r") as aldeas:
        for linea in aldeas:
            partes = linea.strip().split(", ")
            aldea1 = partes[0]
            lista_aldeas.add(aldea1)
    
    # Crea el grafo
    grafo = Grafo()
    with open("aldeas.txt", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split(", ")
            if len(partes) == 3:
                aldea_de = partes[0]
                aldea_a = partes[1]
                try:
                    ponderacion = int(partes[2])
                    grafo.agregar_arista(aldea_de, aldea_a, ponderacion)
                except ValueError:
                    print(f"Error de conversión en la línea: {linea.strip()}")
            else:
                print(f"Formato incorrecto en la línea: {linea.strip()}")
    
    # e envia desde la aldea de inicio
    aldea_inicio = grafo.obtener_vertice('Peligros')
    if aldea_inicio is None:
        print("La aldea de inicio 'Peligros' no se encuentra en el grafo.")
        return
    
    # Ejecuta Prim para encontrar el árbol de expansión mínima
    p(grafo, aldea_inicio)
    
    # Calcula la suma de todas las distancias recorridas
    total_distancia = sum(vertice.obtener_ponderacion(vertice.obtener_predecesor()) for vertice in grafo if vertice.obtener_predecesor() is not None)
    
    # Mostrar los resultados
    print("\nLista de aldeas en orden alfabético:")
    for aldea in sorted(lista_aldeas):
        print(aldea)
    
    print("\nResultados del envío de noticias:")
    for vertice in grafo:
        if vertice.obtener_predecesor() is not None:
            print(f"{vertice.obtener_id()} recibe la noticia de {vertice.obtener_predecesor().obtener_id()}")
            vecinos = [v.id for v in grafo if v != vertice and v.obtener_predecesor() == vertice]
            print(f"   Enviará noticias a: {' '.join(vecinos)}")
    
    print(f"\nTotal de distancia recorrida por todas las palomas: {total_distancia}")

if __name__ == "__main__":
    main()
