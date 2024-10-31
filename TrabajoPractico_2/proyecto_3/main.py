from modules.Grafo import Grafo
from modules.Prim import prim as p

def main():
    # Lee las aldeas del archivo
    lista_aldeas = set()
    with open("aldeas.txt", "r", encoding="UTF-8") as aldeas:
        for linea in aldeas:
            partes = linea.strip().split(", ")
            aldea1 = partes[0]
            lista_aldeas.add(aldea1)
    
    # Crea el grafo
    grafo = Grafo()
    with open("aldeas.txt", "r", encoding="UTF-8") as archivo:
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
    
    # Se envia desde la aldea de inicio
    aldea_inicio = grafo.obtener_vertice('Peligros')
    if aldea_inicio is None:
        print("La aldea de inicio 'Peligros' no se encuentra en el grafo.")
        return
    
    # Ejecuta Prim para encontrar el árbol de expansión mínima
    arbol_expansion = p(grafo, aldea_inicio)
    
    # Mostrar los resultados
    print("\nLista de aldeas en orden alfabético:")
    for aldea in sorted(lista_aldeas):
        print(aldea)
    
    print("\nResultados del envío de noticias:")
    total_distancia = 0
    
    # Para cada vértice en el grafo
    for vertice in grafo:
        predecesor = vertice.obtener_predecesor()
        if predecesor is not None:
            # Obtener la distancia entre el vértice y su predecesor
            distancia = vertice.obtener_ponderacion(predecesor)
            total_distancia += distancia
            
            # Encontrar los vecinos que tienen a este vértice como predecesor
            vecinos = [v.obtener_id() for v in grafo if v.obtener_predecesor() == vertice]
            
            print(f"{vertice.obtener_id()} recibe la noticia de {predecesor.obtener_id()} (distancia: {distancia})")
            if vecinos:
                print(f"   Enviará noticias a: {', '.join(vecinos)}")
            else:
                print("   No enviará noticias a ninguna aldea")
    
    print(f"\nTotal de distancia recorrida por todas las palomas: {total_distancia}")

if __name__ == "__main__":
    main()
