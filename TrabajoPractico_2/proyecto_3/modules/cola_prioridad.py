from modules.monticulo_binario import monticuloBinario

class colaPrioridad:
    def __init__(self):
        self.cola_prioridad = monticuloBinario()
        
    def lista_de_prioridad(self):
        return self.cola_prioridad.listaMonticulo
        
    def insertar(self,k):
        return self.cola_prioridad.insertar(k)
    
    def extraer_mayor_prioridad(self):
        return self.cola_prioridad.eliminarMin()
    
    def tamanio(self):
        return self.cola_prioridad.tamanoActual
    
    def contiene(self, vertice):
        return any(v == vertice for _, v in self.cola_prioridad.listaMonticulo)
    
    def decrementar_clave(self, vertice, nueva_distancia):
        # Busca el vértice en el montículo y actualiza su distancia
        for i in range(1, self.cola_prioridad.tamanoActual + 1):
            if self.cola_prioridad.listaMonticulo[i][1] == vertice:
                # Actualiza la distancia y restablece el orden del montículo
                self.cola_prioridad.listaMonticulo[i] = (nueva_distancia, vertice)
                self.cola_prioridad.infiltArriba(i)
                break
    
    