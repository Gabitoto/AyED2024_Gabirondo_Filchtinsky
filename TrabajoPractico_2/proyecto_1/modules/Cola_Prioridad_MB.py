class cola_Prioridad:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0
    
    def infiltArriba(self, i):
        while i // 2 > 0:  
            if self.listaMonticulo[i].riesgo < self.listaMonticulo[i // 2].riesgo:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2  
             
    def insertar(self,k):
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)
        
    def infiltAbajo(self,i):
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i].riesgo > self.listaMonticulo[hm].riesgo:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm
            
    def hijoMin(self,i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2].riesgo < self.listaMonticulo[i*2+1].riesgo:
                return i * 2
            else:   
                return i * 2 + 1
    
    def eliminarMin(self):
        if self.tamanoActual == 0:
            return None
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.listaMonticulo.pop()  # Elimina el último elemento
        self.tamanoActual -= 1
        self.infiltAbajo(1)
        return valorSacado


