from modules.AVL import NodoArbol,ArbolBinarioBusqueda
from datetime import datetime 

class Temperaturas_DB:
    def __init__(self):
        self.base_de_datos = ArbolBinarioBusqueda()
        self.tamanio = 0
        
    def guardar_temperatura(self,temperatura, fecha):
        """guarda la medida de temperatura asociada a la fecha."""
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        self.base_de_datos._agregar(fecha_dt, temperatura)
        self.tamanio += 1
           
    def devolver_temperatura(self,fecha): 
        """devuelve la medida de temperatura en la fecha determinada."""
        convertir_fecha = datetime.strptime(fecha,"%d/%m/%Y")
        temp = self.mediciones.obtener(convertir_fecha)
        return temp
    
    def max_temp_rango(fecha1, fecha2): 
        """devuelve la temperatura máxima entre los rangos"""
        pass
    
    def fecha1_y_fecha2_inclusive(fecha1,fecha2):
        """Esto no implica que los intervalos del rango deban ser fechas incluidas previamente en el árbol."""
        pass
    
    def min_temp_rango(fecha1, fecha2): 
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