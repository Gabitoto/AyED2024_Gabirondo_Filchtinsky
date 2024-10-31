class monticuloBinario:
    def __init__(self):
        self.listaMonticulo = [(0,0)]
        self.tamanoActual = 0
    
    def construir_monticulo(self,una_lista):
        i = len(una_lista) // 2
        self.tamanoActual = len(una_lista)
        self.listaMonticulo = [0] + una_lista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1
    
    def infiltArriba(self, i):
        while i // 2 > 0:  
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            else:
                break
            i = i // 2  
             
    def insertar(self,k):
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)
        
    def infiltAbajo(self,i):
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm
            
    def hijoMin(self,i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
                return i * 2
            else:   
                return i * 2 + 1
    
    def eliminarMin(self):
        if self.tamanoActual == 0:
            return None
        valorSacado = self.listaMonticulo[1][1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual -= 1  
        self.listaMonticulo.pop() # Elimina el último elemento
        self.infiltAbajo(1)
        return valorSacado
    
    def __iter__(self):
        for i in self.listaMonticulo:
            yield i
    
    def esta_vacia(self):
        if self.tamanoActual == 0:
            return True
        else:
            return False
        
    def __lt__(self, otro):
        return True
    
    def __str__(self):
        return str(self.listaMonticulo)
    
    def __len__(self):
        return self.tamanoActual
    
    def decrementar_clave(self, vertice, nueva_distancia):
        # Busca el vértice en el montículo y actualiza su distancia
        for i in range(1, self.tamanoActual + 1):
            if self.listaMonticulo[i][1] == vertice:
                # Actualiza la distancia y restablece el orden del montículo
                self.listaMonticulo[i] = (nueva_distancia, vertice)
                self.infiltArriba(i)
                break