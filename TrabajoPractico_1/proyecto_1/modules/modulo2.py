# Actividad numero 2: TAD Lista Doblemente Enlazada

# Clase Nodo la cual va tener 3 componentes: el valor, la referencia al siguiente nodo y una referencia al anterior nodo.

class Node:
    
    def __init__(self,valor):
        self.value = valor
        self.next = None
        self.prev = None

# Clase ListaDobleEnlazada desde donde se manejaran las acciones o metodos.

class ListaDobleEnlazda:
    
    def __init__(self):
        self.cabeza = None
        self.cola = None
        
        