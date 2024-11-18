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
    
    def empalmar(self):
       if self.esHoja():
           if self.esHijoIzquierdo():
                  self.padre.hijoIzquierdo = None
           else:
                  self.padre.hijoDerecho = None
       elif self.tieneAlgunHijo():
           if self.tieneHijoIzquierdo():
                  if self.esHijoIzquierdo():
                     self.padre.hijoIzquierdo = self.hijoIzquierdo
                  else:
                     self.padre.hijoDerecho = self.hijoIzquierdo
                  self.hijoIzquierdo.padre = self.padre
           else:
                  if self.esHijoIzquierdo():
                     self.padre.hijoIzquierdo = self.hijoDerecho
                  else:
                     self.padre.hijoDerecho = self.hijoDerecho
                  self.hijoDerecho.padre = self.padre
    
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

    def eliminar(self,clave):
      if self.tamano > 1:
         nodoAEliminar = self._obtener(clave,self.raiz)
         if nodoAEliminar:
             self.remover(nodoAEliminar)
             self.tamano = self.tamano-1
         else:
             raise KeyError('Error, la clave no está en el árbol')
      elif self.tamano == 1 and self.raiz.clave == clave:
         self.raiz = None
         self.tamano = self.tamano - 1
      else:
         raise KeyError('Error, la clave no está en el árbol')

    def __delitem__(self,clave):
       self.eliminar(clave)
      
    def encontrarSucesor(self, nodo):
        if nodo.tieneHijoDerecho():
            return self.encontrarMin(nodo.hijoDerecho)
        else:
            actual = nodo
            while actual.padre and actual.esHijoDerecho():
                actual = actual.padre
            return actual.padre  

    def encontrarMin(self, nodo):
        actual = nodo
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual

    def remover(self,nodoActual):
         padre = nodoActual.padre
         if nodoActual.esHoja(): #hoja
           if nodoActual == nodoActual.padre.hijoIzquierdo:
               nodoActual.padre.hijoIzquierdo = None
           else:
               nodoActual.padre.hijoDerecho = None
         elif nodoActual.tieneAmbosHijos(): #interior
           suc = self.encontrarSucesor(nodoActual)
           suc.empalmar()
           nodoActual.clave = suc.clave
           nodoActual.valor = suc.valor

         else: # este nodo tiene un (1) hijo
           if nodoActual.tieneHijoIzquierdo():
             if nodoActual.esHijoIzquierdo():
                 nodoActual.hijoIzquierdo.padre = nodoActual.padre
                 nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
             elif nodoActual.esHijoDerecho():
                 nodoActual.hijoIzquierdo.padre = nodoActual.padre
                 nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
             else:
                 nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave,
                                    nodoActual.hijoIzquierdo.valor,
                                    nodoActual.hijoIzquierdo.hijoIzquierdo,
                                    nodoActual.hijoIzquierdo.hijoDerecho)
           else:
             if nodoActual.esHijoIzquierdo():
                 nodoActual.hijoDerecho.padre = nodoActual.padre
                 nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
             elif nodoActual.esHijoDerecho():
                 nodoActual.hijoDerecho.padre = nodoActual.padre
                 nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
             else:
                 nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave,
                                    nodoActual.hijoDerecho.valor,
                                    nodoActual.hijoDerecho.hijoIzquierdo,
                                    nodoActual.hijoDerecho.hijoDerecho)
         if padre:
            self.rebalancear_eliminacion(padre)
    
    def rebalancear_eliminacion(self, nodo):
        while nodo:
            if nodo.factorEquilibrio > 1:
                # Rotación a la derecha
                if nodo.hijoDerecho.factorEquilibrio >= 0:
                    self.rotarIzquierda(nodo)
                else:
                    # Rotación doble
                    self.rotarDerecha(nodo.hijoDerecho)
                    self.rotarIzquierda(nodo)
            elif nodo.factorEquilibrio < -1:
                # Rotación a la izquierda
                if nodo.hijoIzquierdo.factorEquilibrio <= 0:
                    self.rotarDerecha(nodo)
                else:
                    # Rotación doble
                    self.rotarIzquierda(nodo.hijoIzquierdo)
                    self.rotarDerecha(nodo)
            
            # Actualizar factor de equilibrio
            if nodo.factorEquilibrio == 0:
                # Si el factor de equilibrio llega a 0, paramos
                break
            
            # Subir al padre
            nodo = nodo.padre
            
    def removerNodoSucesor(self, nodo):
        # Si el nodo sucesor es una hoja
        if nodo.esHoja():
            if nodo.esHijoIzquierdo():
                nodo.padre.hijoIzquierdo = None
            else:
                nodo.padre.hijoDerecho = None
        # Si el nodo sucesor tiene solo hijo derecho
        elif nodo.tieneHijoDerecho():
            if nodo.esHijoIzquierdo():
                nodo.padre.hijoIzquierdo = nodo.hijoDerecho
            else:
                nodo.padre.hijoDerecho = nodo.hijoDerecho
            nodo.hijoDerecho.padre = nodo.padre

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
