# Actividad numero 2: TAD Lista Doblemente Enlazada

# Clase Nodo la cual va tener 3 componentes: el valor, la referencia al siguiente nodo y una referencia al anterior nodo.

class Node:
    
    def __init__(self,valor):
        self.dato = valor
        self.siguiente = None
        self.anterior = None
    
    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

# Clase ListaDobleEnlazada desde donde se manejaran las acciones o metodos.

class ListaDobleEnlazada:
    
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
        
    def esta_vacia(self): 
        """Devuelve True si la lista está vacía."""
        return self.tamanio == 0
    
    def limpiar(self):
        """Funcion que limpia la lista de todos los nodos o items"""
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
        
    def __len__(self):
        """Devuelve el número de ítems de la lista."""
        return self.tamanio
        
        
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
        self.tamanio += 1
        
    
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
        self.tamanio += 1
            
    def insertar(self,item, posicion = None):
        """Agrega un nuevo ítem a la lista en "posicion". Si la posición no se pasa como argumento, el ítem debe añadirse al final de la lista. 
        "posicion" es un entero que indica la posición en la lista donde se va a insertar el nuevo elemento. 
        Si se quiere insertar en una posición inválida, que se arroje la debida excepción."""
        
        nodo_a_insertar = Node(item)
        
        if self.esta_vacia() or posicion == 0:
            self.agregar_al_inicio(item)
            return
        
        if posicion is None:
            self.agregar_al_final(item)
            return
        
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posicion fuera de rango")
        
        else:
            nodo_actual = self.cabeza
            for x in range(posicion-1):
                nodo_actual = nodo_actual.siguiente
        
            nodo_a_insertar.siguiente = nodo_actual.siguiente
            nodo_a_insertar.anterior = nodo_actual
            
            if nodo_actual.siguiente is not None:
                nodo_actual.siguiente.anterior = nodo_a_insertar
                nodo_actual.siguiente = nodo_a_insertar
            if posicion == self.tamanio:
                self.cola = nodo_a_insertar
            
        self.tamanio += 1
                 
        
    def extraer(self, posicion = None):
        """elimina y devuelve el ítem en "posición". Si no se indica el parámetro
        posición, se elimina y devuelve el último elemento de la lista. La complejidad de extraer
        elementos de los extremos de la lista debe ser O(1). Si se quiere extraer de una posición
        indebida, que se arroje la debida excepción."""
        if self.esta_vacia():
            raise IndexError("No se puede extraer de un lista vacia")
        
        if posicion is not None and (posicion < -1 or posicion >= self.tamanio):
            raise IndexError("Índice fuera de rango")
        
        if posicion == 0:
            valor = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza is not None:
                self.cabeza.anterior = None
            else:
                self.cola = None
            self.tamanio -= 1
            return valor
        
        if posicion is None or posicion == self.tamanio - 1 or posicion == -1:
            valor = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola is not None:
                self.cola.siguiente = None
            else:
                self.cabeza = None
            self.tamanio -= 1
            return valor
        
        else:
            nodo_actual = self.cabeza
            for _ in range(posicion):
                nodo_actual = nodo_actual.siguiente
    
            valor = nodo_actual.dato
            nodo_actual.anterior.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente.anterior = nodo_actual.anterior
    
        self.tamanio -= 1
        return valor
        
        
    def copiar(self):
        """Realiza una copia de la lista elemento a elemento y devuelve la copia. Verificar
        que el orden de complejidad de este método sea O(n) y no O(n2)."""
        nueva_lista = ListaDobleEnlazada()
        nodo_actual = self.cabeza

        while nodo_actual is not None:
            nueva_lista.agregar_al_final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

        return nueva_lista
    
    def invertir(self): # Explicar despues
        """Invierte el orden de los elementos de la lista."""
        actual_nodo = self.cabeza
        while actual_nodo is not None:
            temp = actual_nodo.siguiente
            actual_nodo.siguiente = actual_nodo.anterior
            actual_nodo.anterior = temp
            actual_nodo = temp
            
        self.cabeza,self.cola = self.cola,self.cabeza
        return self
    
     
    def concatenar(self,Lista):
        """Recibe una lista como argumento y retorna la lista actual con la lista
        pasada como parámetro concatenada al final de la primera."""
        
        if self.esta_vacia():
            self.cabeza = Lista.cabeza
            self.cola = Lista.cola
        else:
            for item in Lista:
                self.agregar_al_final(item)
        return self
    
    def __add__(self,Lista):
        """El resultado de “sumar” dos listas debería ser una nueva lista con los
        elementos de la primera lista y los de la segunda. Aprovechar el método concatenar para
        evitar repetir código."""
        copia_lista1 = self.copiar()
        return copia_lista1.concatenar(Lista)
    
    def mostrar(self):
        """Funcion que itera sobre la LDE retornando el valor de sus nodos"""
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente
    
    def __iter__(self):
        """ Funcion que nos permite iterar sobre la LDE logrando que nos devuelva sus datos y no el nodo en si obteniendo una eficiencia de Memoria ya que no necesitas almacenar todos los elementos en una lista temporal para iterar sobre ellos y simplicidad por que hace que la clase sea iterable sin necesidad de implementar manualmente __iter__() y __next__()."""
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            yield nodo_actual.dato
            nodo_actual = nodo_actual.siguiente
    

#------------------------------- Llamado a la LDE para probar sus funciones -------------------------------#

dll = ListaDobleEnlazada()
print(dll.esta_vacia())
dll.agregar_al_inicio(10)
dll.agregar_al_inicio(20)
dll.agregar_al_inicio(30)
dll.agregar_al_final(40)
print(dll.esta_vacia())
dll2 = dll.copiar()
print(len(dll2))
print(len(dll))
dll2.concatenar(dll)
print(len(dll2))
dll.mostrar()
print()
dll2.mostrar()
ob = dll + dll2
print(len(ob))
dll.limpiar()
print(dll.esta_vacia())