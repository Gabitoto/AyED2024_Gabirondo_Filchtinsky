class monticuloBinario:
    def __init__(self):
        self.lista_monticulo = [(0, None)]  # Elemento dummy en índice 0
        self.tamano_actual = 0
        self.posiciones = {}  # Diccionario para rastrear posiciones de vértices

    def infiltrar_arriba(self, i):
        while i // 2 > 0:
            if self.lista_monticulo[i][0] < self.lista_monticulo[i // 2][0]:
                # Actualizar posiciones antes del intercambio
                self.actualizar_posicion(self.lista_monticulo[i][1], i // 2)
                self.actualizar_posicion(self.lista_monticulo[i // 2][1], i)
                # Realizar el intercambio
                self.lista_monticulo[i], self.lista_monticulo[i // 2] = \
                    self.lista_monticulo[i // 2], self.lista_monticulo[i]
            i = i // 2

    def infiltrar_abajo(self, i):
        while (i * 2) <= self.tamano_actual:
            hm = self.hijo_min(i)
            if self.lista_monticulo[i][0] > self.lista_monticulo[hm][0]:
                # Actualizar posiciones antes del intercambio
                self.actualizar_posicion(self.lista_monticulo[i][1], hm)
                self.actualizar_posicion(self.lista_monticulo[hm][1], i)
                # Realizar el intercambio
                self.lista_monticulo[i], self.lista_monticulo[hm] = \
                    self.lista_monticulo[hm], self.lista_monticulo[i]
            i = hm

    def insertar(self, k):
        self.lista_monticulo.append(k)
        self.tamano_actual += 1
        self.actualizar_posicion(k[1], self.tamano_actual)
        self.infiltrar_arriba(self.tamano_actual)

    def hijo_min(self, i):
        if i * 2 + 1 > self.tamano_actual:
            return i * 2
        else:
            if self.lista_monticulo[i * 2][0] < self.lista_monticulo[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1

    def eliminarMin(self):
        if len(self.lista_monticulo) <= 1:
            return None
        
        valor_raiz = self.lista_monticulo[1][1]  # Obtener el vértice (no la tupla completa)
        self.actualizar_posicion(self.lista_monticulo[self.tamano_actual][1], 1)
        self.lista_monticulo[1] = self.lista_monticulo[self.tamano_actual]
        self.tamano_actual -= 1
        self.lista_monticulo.pop()
        if self.tamano_actual > 0:
            self.infiltrar_abajo(1)
        
        # Eliminar la posición del vértice eliminado
        if valor_raiz in self.posiciones:
            del self.posiciones[valor_raiz]
            
        return valor_raiz

    def construir_monticulo(self, lista_vert):
        self.tamano_actual = len(lista_vert)
        self.lista_monticulo = [(0, None)] + lista_vert[:]
        # Inicializar las posiciones
        for i in range(1, len(self.lista_monticulo)):
            self.actualizar_posicion(self.lista_monticulo[i][1], i)
        i = len(lista_vert) // 2
        while i > 0:
            self.infiltrar_abajo(i)
            i = i - 1

    def esta_vacia(self):
        return self.tamano_actual == 0

    def decrementar_clave(self, vertice, nueva_dist):
        # Encontrar la posición del vértice
        if vertice not in self.posiciones:
            return
        
        pos = self.posiciones[vertice]
        if pos > self.tamano_actual:
            return
            
        # Actualizar la distancia
        self.lista_monticulo[pos] = (nueva_dist, vertice)
        self.infiltrar_arriba(pos)

    def actualizar_posicion(self, vertice, pos):
        """Actualiza la posición de un vértice en el montículo"""
        if vertice is not None:
            self.posiciones[vertice] = pos

    def __contains__(self, vertice):
        return vertice in self.posiciones