import unittest 
from modules.Temperaturas_DB import Temperaturas_DB
from modules.AVL import ArbolBinarioBusqueda,NodoArbol


class TestTemperaturasDB(unittest.TestCase):
    def setUp(self):
        self.temp = Temperaturas_DB()
        self.cant_temp = 0
        self.lista_fecha = ["21/01/2024","22/01/2024","23/01/2024","24/01/2024"]
        self.temperatura = [24,27,14,10]
        self.fechamin = "21/01/2024"
        self.fechamax = "24/01/2024"
        self.fecha_temp = ("23/01/2024",14)

    

    def test_guardar_temperatura(self):
        for fecha,temp in zip (self.lista_fecha,self.temperatura):
            self.temp.guardar_temperatura(fecha, temp)   
            self.cant_temp +=1
        self.assertEqual(self.temp.tamano, self.cant_temp)



    def test_devolver_temperatura(self):
        self.temp.guardar_temperatura("21/01/2024",24)
        self.temp.guardar_temperatura("22/01/2024",27)
        self.temp.guardar_temperatura("23/01/2024",14)
        self.temp.guardar_temperatura("24/01/2024",10)
        dev = self.temp.devolver_temperatura("23/01/2024")
        self.assertEqual(self.fecha_temp[1],dev)
        

    def test_max_temp_rango(self):
        mayor = 27
        self.fechamin = "21/01/2024"
        self.fechamax = "24/01/2024"
        self.temp.guardar_temperatura("21/01/2024",24)
        self.temp.guardar_temperatura("22/01/2024",27)
        self.temp.guardar_temperatura("23/01/2024",14)
        self.temp.guardar_temperatura("24/01/2024",10)

        dev = self.temp.max_temp_rango(self.fechamin, self.fechamax)
        self.assertEqual(mayor, dev)
    
    

    def test_min_temp_rango(self):
        mini = 10
        self.fechamin = "21/01/2024"
        self.fechamax = "24/01/2024"
        self.temp.guardar_temperatura("21/01/2024",24)
        self.temp.guardar_temperatura("22/01/2024",27)
        self.temp.guardar_temperatura("23/01/2024",14)
        self.temp.guardar_temperatura("24/01/2024",10)
        
        dev = self.temp.min_temp_rango(self.fechamin, self.fechamax)
        self.assertEqual(mini, dev)


    def test_temp_extremos_rango(self):
        mini = 10
        mayor = 27
        self.fechamin = "21/01/2024"
        self.fechamax = "24/01/2024"
        self.temp.guardar_temperatura("21/01/2024",24)
        self.temp.guardar_temperatura("22/01/2024",27)
        self.temp.guardar_temperatura("23/01/2024",14)
        self.temp.guardar_temperatura("24/01/2024",10)
        dev = self.temp.temp_extremos_rango(self.fechamin, self.fechamax)
        self.assertEqual(dev, (mini, mayor))


    def test_borrar_temperatura(self):
        self.temp.guardar_temperatura("21/01/2024",24)
        self.temp.guardar_temperatura("22/01/2024",27)
        self.temp.guardar_temperatura("23/01/2024",14)
        self.temp.guardar_temperatura("24/01/2024",10)
        borrar = "23/01/2024"
        self.temp.borrar_temperatura(borrar)
        buscar = self.temp.devolver_temperatura("23/01/2024")
        self.assertFalse(buscar)



if __name__ == "__main__":
    unittest.main()