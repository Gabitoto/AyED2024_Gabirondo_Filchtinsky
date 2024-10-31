from modules.Vertice import Vertice
 
class Grafo:
    def __init__(self):
        self.lista_vertices = {}
        self.num_vertices = 0
   
    def __getitem__(self, clave):
        return self.obtener_vertice(clave)
    
    def agregar_vertice(self, clave):
        self.num_vertices = self.num_vertices + 1
        nuevo_vertice = Vertice(clave)
        self.lista_vertices[clave] = nuevo_vertice
        return nuevo_vertice

    def obtener_vertice(self, clave):
        if clave in self.lista_vertices:
            return self.lista_vertices[clave]
        else:
            return None

    def __contains__(self, n):
        return n in self.lista_vertices

    def agregar_arista(self, de, a, ponderacion):
        # Agregar vértices si no existen
        if de not in self.lista_vertices:
            self.agregar_vertice(de)
        if a not in self.lista_vertices:
            self.agregar_vertice(a)
        
        # Agregar arista en ambas direcciones (grafo no dirigido)
        self.lista_vertices[de].agregar_vecino(self.lista_vertices[a], ponderacion)
        self.lista_vertices[a].agregar_vecino(self.lista_vertices[de], ponderacion)

    def obtener_vertices(self):
        return self.lista_vertices.values()

    def __iter__(self):
        return iter(self.lista_vertices.values())
    
