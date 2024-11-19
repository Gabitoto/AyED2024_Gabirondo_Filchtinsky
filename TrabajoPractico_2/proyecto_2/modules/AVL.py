class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None):
        self.__clave = clave
        self.__cargaUtil = valor
        self.__hijoIzquierdo = izquierdo
        self.__hijoDerecho = derecho
        self.__padre = padre
        self.__factorEquilibrio = 0

    @property
    def clave(self):
        return self.__clave
    
    @clave.setter
    def clave(self, clave):
        self.__clave = clave
        
    @property
    def valor(self):
        return self.__cargaUtil
    
    @valor.setter
    def valor(self,valor):
        self.__cargaUtil = valor
        
    def tieneHijoIzquierdo(self):
        return self.__hijoIzquierdo
    
    @property
    def hijoIzquierdo(self):
        return self.__hijoIzquierdo
    
    @hijoIzquierdo.setter
    def hijoIzquierdo(self,izquierdo):
        self.__hijoIzquierdo = izquierdo
        
    def tieneHijoDerecho(self):
        return self.__hijoDerecho
    
    @property
    def hijoDerecho(self):
        return self.__hijoDerecho
    
    @hijoDerecho.setter
    def hijoDerecho(self,derecho):
        self.__hijoDerecho = derecho
    
    @property
    def padre(self):
        return self.__padre
    
    @padre.setter
    def padre(self,padre):
        self.__padre = padre
    
    @property
    def factorEquilibrio(self):
        return self.__factorEquilibrio
    
    @factorEquilibrio.setter
    def factorEquilibrio(self, valor):
        self.__factorEquilibrio = valor  # Asigna el valor directamente 

    def sumar_factor(self, valor): # Método para sumar al factor de equilibrio
        self.__factorEquilibrio += valor

    def restar_factor(self, valor): # Método para restar al factor de equilibrio
        self.__factorEquilibrio -= valor
    
    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self
    
    def __iter__(self):
        if self:
            if self.tieneHijoIzquierdo():
                    for elem in self.hijoIzquierdo:
                        yield elem
            yield self.clave
            if self.tieneHijoDerecho():
                    for elem in self.hijoDerecho:
                        yield elem
    
    
    def imprimir_nodo(self):
        print(f"Fecha: {self.clave}, Temperatura: {self.valor}")


class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano

    def agregar(self,clave,valor):
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            self.raiz = NodoArbol(clave,valor)
        self.tamano = self.tamano + 1

    def _agregar(self,clave,valor,nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave,valor,nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoDerecho)

    def actualizarEquilibrio(self,nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esHijoIzquierdo():
                nodo.padre.sumar_factor(1)
            elif nodo.esHijoDerecho():
                nodo.padre.restar_factor(1)

            if nodo.padre.factorEquilibrio != 0:
                self.actualizarEquilibrio(nodo.padre)
      
    def rotarIzquierda(self,rotRaiz):
        nuevaRaiz = rotRaiz.hijoDerecho
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo != None:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = rotRaiz
        rotRaiz.padre = nuevaRaiz
        
        rotRaiz.sumar_factor(1 - min(nuevaRaiz.factorEquilibrio, 0))
        nuevaRaiz.sumar_factor(1)
        nuevaRaiz.restar_factor(max(rotRaiz.factorEquilibrio, 0))
    
    def rotarDerecha(self,rotRaiz):
        nuevaRaiz = rotRaiz.hijoIzquierdo
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho!= None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoDerecho():
                rotRaiz.padre.hijoDerecho = nuevaRaiz
            else:
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
        nuevaRaiz.hijoDerecho = rotRaiz
        rotRaiz.padre = nuevaRaiz
        
        rotRaiz.restar_factor(1 + max(nuevaRaiz.factorEquilibrio, 0))
        nuevaRaiz.restar_factor(1)
        nuevaRaiz.sumar_factor(min(rotRaiz.factorEquilibrio, 0))
    
    def reequilibrar(self,nodo):
        if nodo.factorEquilibrio < 0:
           if nodo.hijoDerecho.factorEquilibrio > 0:
              self.rotarDerecha(nodo.hijoDerecho)
              self.rotarIzquierda(nodo)
           else:
              self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
           if nodo.hijoIzquierdo.factorEquilibrio < 0:
              self.rotarIzquierda(nodo.hijoIzquierdo)
              self.rotarDerecha(nodo)
           else:
              self.rotarDerecha(nodo)
    
    def __setitem__(self,c,v):
       self.agregar(c,v)

    def obtener(self,clave):
       if self.raiz:
           res = self._obtener(clave,self.raiz)
           if res:
                  return res.valor
           else:
                  return None
       else:
           return None

    def _obtener(self,clave,nodoActual):
       if not nodoActual:
           return None
       elif nodoActual.clave == clave:
           return nodoActual
       elif clave < nodoActual.clave:
           return self._obtener(clave,nodoActual.hijoIzquierdo)
       else:
           return self._obtener(clave,nodoActual.hijoDerecho)

    def __getitem__(self,clave):
       return self.obtener(clave)

    def __contains__(self,clave):
       if self._obtener(clave,self.raiz):
           return True
       else:
           return False
         
    def eliminar(self, clave):
        nodo = self._obtener(clave, self.raiz)
        if nodo is None:
            raise KeyError(f"La clave {clave} no existe en el árbol")
        
        # Guardar el padre antes de eliminar para actualizar el equilibrio después
        padre_original = nodo.padre
        
        # Caso 1: Nodo hoja
        if nodo.esHoja():
            if nodo == self.raiz:
                self.raiz = None
            else:
                padre = nodo.padre
                if nodo.esHijoIzquierdo():
                    padre.hijoIzquierdo = None
                    padre.restar_factor(1)
                else:
                    padre.hijoDerecho = None
                    padre.sumar_factor(1)
                
                # Actualizar el equilibrio desde el padre
                if padre.factorEquilibrio != 0:
                    self.actualizarEquilibrio(padre)
        
        # Caso 2: Nodo con un hijo
        elif nodo.hijoIzquierdo is None:  # tiene hijo derecho
            if nodo == self.raiz:
                self.raiz = nodo.hijoDerecho
                self.raiz.padre = None
            else:
                padre = nodo.padre
                hijo = nodo.hijoDerecho
                if nodo.esHijoIzquierdo():
                    padre.hijoIzquierdo = hijo
                else:
                    padre.hijoDerecho = hijo
                hijo.padre = padre
                
                # Actualizar el equilibrio
                padre.restar_factor(1)
                if padre.factorEquilibrio != 0:
                    self.actualizarEquilibrio(padre)
        
        elif nodo.hijoDerecho is None:  # tiene hijo izquierdo
            if nodo == self.raiz:
                self.raiz = nodo.hijoIzquierdo
                self.raiz.padre = None
            else:
                padre = nodo.padre
                hijo = nodo.hijoIzquierdo
                if nodo.esHijoIzquierdo():
                    padre.hijoIzquierdo = hijo
                else:
                    padre.hijoDerecho = hijo
                hijo.padre = padre
                
                # Actualizar el equilibrio
                padre.sumar_factor(1)
                if padre.factorEquilibrio != 0:
                    self.actualizarEquilibrio(padre)
        
        # Caso 3: Nodo con dos hijos
        else:
            # Encontrar el sucesor (el menor del subárbol derecho)
            sucesor = self.encontrarMin(nodo.hijoDerecho)
            # Guardar los valores del sucesor
            temp_clave = sucesor.clave
            temp_valor = sucesor.valor
            # Eliminar el sucesor recursivamente
            self.eliminar(sucesor.clave)
            # Copiar los valores del sucesor al nodo actual
            nodo.clave = temp_clave
            nodo.valor = temp_valor
        
        # Decrementar el tamaño del árbol
        self.tamano -= 1

    def __delitem__(self,clave):
       self.eliminar(clave)
      
    def encontrarMin(self, nodo):
        actual = nodo
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual
    
    def in_order_generator(self, nodo):
        """Generador que recorre el árbol AVL en in-order."""
        if nodo is not None:
            # Recorrer el subárbol izquierdo
            yield from self.in_order_generator(nodo.hijoIzquierdo)
            # Devolver el nodo actual
            yield nodo
            # Recorrer el subárbol derecho
            yield from self.in_order_generator(nodo.hijoDerecho)
    
    def iterar_en_orden(self):
        """Inicia la iteración sobre el árbol AVL desde la raíz."""
        return self.in_order_generator(self.raiz)
