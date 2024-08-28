# Actividad numero 2: TAD Lista Doblemente Enlazada

# Clase Nodo la cual va tener 3 componentes: el valor, la referencia al siguiente nodo y una referencia al anterior nodo.

class Node:
    
    def __init__(self,valor):
        self.dato = valor
        self.siguiente = None
        self.anterior = None

# Clase ListaDobleEnlazada desde donde se manejaran las acciones o metodos.

class ListaDobleEnlazada:
    
    def __init__(self):
        self.cabeza = None
        self.cola = None
        
    def esta_vacia(self): 
        """Devuelve True si la lista está vacía."""
        return self.cabeza is None and self.cola is None
    
    def limpiar(self):
        """Funcion que limpia la lista de todos los nodos o items"""
        self.cabeza = None
        self.cola = None
        
    def __len__(self):
        """Devuelve el número de ítems de la lista."""
        count = 0 # iniciamos el contador
        actual = self.cabeza # asignamos una variable con la referencia a la cabeza de la lista
        while actual: # la recorremos y cada vez que nos posicionamos en un nodo agregamos +1 al contador y referenciamos al siguiente nodo
            count += 1
            actual = actual.siguiente
        return count # retornamos el numero de nodos recorridos
        
        
    def agregar_al_inicio(self,item): 
        """Agrega un nuevo ítem al inicio de la lista."""
        nuevo_nodo = Node(item)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza # El next del nuevo_nodo apunta al nodo que actualmente es la cabeza de la lista.
            self.cabeza.anterior = nuevo_nodo # El prev del nodo que actualmente es la cabeza de la lista se actualiza para que apunte al nuevo_nodo.
            self.cabeza = nuevo_nodo # Finalmente, la cabeza de la lista se actualiza para que apunte al nuevo_nodo.
        
    
    def agregar_al_final(self,item): 
        """Agrega un nuevo ítem al final de la lista."""
        nuevo_nodo = Node(item)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola # El nuevo nodo se a punta a la cola de la lista.
            self.cola.siguiente = nuevo_nodo # La referencia de la cola anterior se apunta al nuevo nodo.
            self.cola = nuevo_nodo # y finalmente se actualiza la cola de la lista para que almacene el nuevo nodo.
            
    def insertar(item, posicion):
        """Agrega un nuevo ítem a la lista en "posicion". Si la posición no se pasa como argumento, el ítem debe añadirse al final de la lista. "posicion" es un
        entero que indica la posición en la lista donde se va a insertar el nuevo elemento. Si se
        quiere insertar en una posición inválida, que se arroje la debida excepción."""
        
    def extraer(posicion):
        """elimina y devuelve el ítem en "posición". Si no se indica el parámetro
        posición, se elimina y devuelve el último elemento de la lista. La complejidad de extraer
        elementos de los extremos de la lista debe ser O(1). Si se quiere extraer de una posición
        indebida, que se arroje la debida excepción."""
        
    def copiar(self):
        """Realiza una copia de la lista elemento a elemento y devuelve la copia. Verificar
        que el orden de complejidad de este método sea O(n) y no O(n2)."""
        nueva_lista = ListaDobleEnlazada()
        nodo_actual = self.cabeza

        while nodo_actual is not None:
            nueva_lista.agregar_al_final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

        return nueva_lista
    
    def invertir():
        """Invierte el orden de los elementos de la lista."""
        
    def concatenar(Lista):
        """Recibe una lista como argumento y retorna la lista actual con la lista
        pasada como parámetro concatenada al final de la primera."""
    
    def __add__(Lista):
        """El resultado de “sumar” dos listas debería ser una nueva lista con los
        elementos de la primera lista y los de la segunda. Aprovechar el método concatenar para
        evitar repetir código."""
    
    def mostrar(self):
        """Funcion que itera sobre la LDE retornando el valor de sus nodos"""
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente

#------------------------------- Llamado a la LDE para probar sus funciones -------------------------------#

dll = ListaDobleEnlazada()
print(dll.esta_vacia())
dll.agregar_al_inicio(10)
dll.agregar_al_inicio(20)
dll.agregar_al_inicio(30)
dll.agregar_al_final(40)
print(dll.esta_vacia())
print(len(dll))
dll.mostrar()
dll.limpiar()
print(dll.esta_vacia())


