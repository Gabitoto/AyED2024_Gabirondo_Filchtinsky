from modules.monticulo_binario import monticuloBinario

class colaPrioridad:
    
    def __init__(self):
        self.cola_prioridad = monticuloBinario()
        
    def lista_de_prioridad(self):
        return self.cola_prioridad.listaMonticulo
        
    def insertar(self,k):
        self.cola_prioridad.insertar(k)
    
    def extraer_mayor_prioridad(self):
        self.cola_prioridad.eliminarMin()
    
    def esta_vacio(self):
        if self.tamanio == 0:
            return None
    
    def tamanio(self):
        return self.cola_prioridad.tamanoActual