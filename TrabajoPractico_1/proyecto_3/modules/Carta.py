
# Clase Carta = Clase que se comportara como nuestro Nodo.
class Carta:
    
    def __init__(self, dato='', palo='', carta_arriba = None, carta_abajo = None):
        self.dato = dato
        self.palo = palo
        self.visible:bool = False
        self.carta_arriba = carta_arriba
        self.carta_abajo = carta_abajo
        
    def asignar_arriba(self, carta):
        self.carta_arriba = carta
        
    def asignar_abajo(self, carta):
        self.carta_abajo = carta
        
# Decoradores = Los decoradores en Python son una manera de modificar el comportamiento de funciones o métodos sin alterar directamente su código. Se usan comúnmente para reutilizar lógica, como agregar validaciones o realizar tareas antes o después de que una función se ejecute.
# Los decoradores son funciones que reciben como argumento otra función o método, le añaden comportamiento y devuelven una nueva función con esa modificación.
        
    @property  # Este convierte métodos en "atributos calculados". Esto permite que accedamos a métodos como si fueran atributos normales, pero con la capacidad de añadir lógica al obtener o asignar valores.
    def visible(self):
        return self._visible
        
    @visible.setter # Este decorador indica que este método es el "setter", es decir, define lo que ocurre cuando intentas asignar un valor al atributo visible.
    def visible(self, visible):
        if not isinstance(visible, bool): # Aquí el setter verifica si el valor es un booleano antes de asignarlo, proporcionando una capa de seguridad sin cambiar el código que usa el atributo.
            raise ValueError("visible debe ser True o False")
        self._visible = visible
        
    @property
    def dato(self):
        return self._dato
    
    @dato.setter
    def dato(self, dato):
        self._dato = dato
        
    @property
    def palo(self):
        return self._palo
    
    @palo.setter
    def palo(self, palo):
        self._palo = palo  
    
    def _valor_numerico(self):
        """Agrega valor numerico a las cartas que posean valores por encima del 10 y se representen con letras."""
        valores = ['J','Q','K','A']
        if self.dato in valores:
            idx = valores.index(self.dato)
            return (11 + idx)
        return int(self.dato)            
            
        
    def __gt__(self, otra):
        """2 cartas deben compararse por su valor numérico"""
        return self._valor_numerico() > otra._valor_numerico()
        
    def __str__(self):
        """Funcion que permite settear si una carta es visible o no en caso de que sea visible se mostrara su carga util en caso de que no un "-X"."""
        if self.visible == False:
            return "-X"
        else:
            return f"{self.dato} {self.palo}"
    
    def __repr__(self):
        return str(self)
    
    
if __name__ == "__main__":
    carta = Carta("♣", "3")
    print(carta)
    carta.visible = True
    print(carta) 