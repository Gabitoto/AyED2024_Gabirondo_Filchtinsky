class Nodo:
    def __init__(self,carga_util,altura,hijoizq,hijoder):
        self.dato = carga_util
        self.padre = None
        self.altura = altura
        self.hijoizq = hijoizq
        self.hijoder = hijoder

    def obtenerDato(self):
        return self.dato

    def obtenerPadre(self):
        return self.padre

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente