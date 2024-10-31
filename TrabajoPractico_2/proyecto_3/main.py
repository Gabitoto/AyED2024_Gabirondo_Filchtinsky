from modules.Grafo import Grafo
from modules.Prim import prim as p

def main():
    # Lee las aldeas del archivo
    lista_aldeas = set()
    with open("TrabajoPractico_2/proyecto_3/data/aldeas.txt", "r", encoding="UTF-8") as aldeas:
        for linea in aldeas:
            partes = linea.strip().split(", ")
            aldea1 = partes[0]
            lista_aldeas.add(aldea1)
    
    # Crea el grafo
    grafo = Grafo()
    with open("TrabajoPractico_2/proyecto_3/data/aldeas.txt", "r", encoding="UTF-8") as archivo:
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
    flujo_mensajes, aldeas_recorridas = p(grafo, aldea_inicio)
    
    # Calcular distancia total
    distancia_total = sum(mensaje['distancia'] for mensaje in flujo_mensajes)
    
    # Mostrar el flujo de mensajes con numeración
    print("\nFlujo de mensajes:")
    for i, mensaje in enumerate(flujo_mensajes, 1):
        print(f"{i}. {mensaje['emisor']} a {mensaje['receptor']} (distancia: {mensaje['distancia']})")
    
    # Mostrar aldeas en orden alfabético
    print("\nAldeas recorridas (orden alfabético):")
    for aldea in sorted(aldeas_recorridas):
        print(aldea)
    
    # Mostrar distancia total
    print(f"\nDistancia total recorrida: {distancia_total}")

if __name__ == "__main__":
    main()