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