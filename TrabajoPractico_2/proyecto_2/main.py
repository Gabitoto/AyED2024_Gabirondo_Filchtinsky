from modules.AVL import NodoArbol,ArbolBinarioBusqueda
from datetime import datetime 

class Temperaturas_DB:
    def __init__(self):
        self.base_de_datos = ArbolBinarioBusqueda()
        self.tamano = 0
        
    def guardar_temperatura(self, fecha, temperatura):
        """guarda la medida de temperatura asociada a la fecha."""
        self.base_de_datos.agregar(fecha, temperatura)
        self.tamano += 1
           
    def devolver_temperatura(self,fecha): 
        """devuelve la medida de temperatura en la fecha determinada."""
        temp = self.base_de_datos.obtener(fecha)
        return temp
    
    def max_temp_rango(self, fecha1, fecha2): 
        """devuelve la temperatura máxima entre los rangos, fecha1 y fecha2 inclusive (fecha1,fecha2).
        Esto no implica que los intervalos del rango deban ser fechas incluidas previamente en el árbol."""
        pass
    
    def min_temp_rango(self, fecha1, fecha2): 
        """devuelve la temperatura mínima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2).
        Esto no implica que los intervalos del rango deban ser fechas incluidas previamente en el árbol."""
        pass
    
    def temp_extremos_rango(fecha1, fecha2): 
        """devuelve la temperatura mínima y máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2)."""
        pass
    
    def borrar_temperatura(fecha): 
        """recibe una fecha y elimina del árbol la medición correspondiente a esa fecha."""
        pass
    
    def devolver_temperaturas(fecha1, fecha2): 
        """devuelve un listado de las mediciones de temperatura en el rango recibido por parámetro con el formato “dd/mm/aaaa: temperatura
        ºC”, ordenado por fechas."""
        pass
    
    def cantidad_muestras(self): 
        """devuelve la cantidad de muestras de la BD."""
        return self.tamanio
    
    