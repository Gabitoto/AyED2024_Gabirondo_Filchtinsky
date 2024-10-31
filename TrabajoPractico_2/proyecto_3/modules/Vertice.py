class Vertice:
    def __init__(self, clave, dist=0):
        self.id = clave
        self.conectado_a = {}  # Ahora almacenará objetos Vertice como claves
        self.dist = dist
        self.predecesor = None
        
    def asignar_distancia(self, valor):
        self.dist = valor
        
    def obtener_distancia(self):
        return self.dist
    
    def agregar_vecino(self, vecino, ponderacion):
        """
        Agrega un vecino al vértice actual
        vecino: objeto Vertice
        ponderacion: peso de la arista
        """
        self.conectado_a[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectado a: ' + str([x.id for x in self.conectado_a]) + ' con pesos: ' + str([self.conectado_a[v] for v in self.conectado_a])

    def obtener_conexiones(self):
        """Devuelve una lista con todos los vértices conectados"""
        return self.conectado_a.keys()

    def obtener_id(self):
        return self.id

    def obtener_ponderacion(self, vecino):
        """
        Obtiene la ponderación de la arista que conecta con el vecino
        vecino: objeto Vertice
        """
        return self.conectado_a.get(vecino, float('inf'))
    
    def asignar_predecesor(self, predecesor):
        self.predecesor = predecesor
    
    def obtener_predecesor(self):
        return self.predecesor
    
    def __lt__(self, otro):
        return self.dist < otro.dist
    
    def __eq__(self, otro):
        if isinstance(otro, Vertice):
            return self.id == otro.id
        return False
    
    def __hash__(self):
        return hash(self.id)
        
