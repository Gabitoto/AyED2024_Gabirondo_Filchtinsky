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
    
    def decrementarClave(self,vertice,nueva_distancia):
        # se busca el vertice en la cola de prioridad y actualiza su distancia
        for i, (distancia,v) in enumerate(self.cola_prioridad.listaMonticulo):
            if v == vertice:
                self.cola_prioridad.listaMonticulo[i] = (nueva_distancia,vertice) # actualiza la distancia
                break
        self.cola_prioridad.listaMonticulo.sort(key=lambda x: x[0]) # ordena por distancia