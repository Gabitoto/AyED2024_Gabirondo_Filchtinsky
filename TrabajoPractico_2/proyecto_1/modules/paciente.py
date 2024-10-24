# -*- coding: utf-8 -*-

from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
        def __init__(self):
            n = len(nombres)
            self.__nombre = nombres[randint(0, n-1)]
            self.__apellido = apellidos[randint(0, n-1)]
            self.riesgo = choices(niveles_de_riesgo, probabilidades)[0]
            self.__descripcion = descripciones_de_riesgo[self.riesgo-1]

        def get_nombre(self):
            return self.__nombre

        def get_apellido(self):
            return self.__apellido

        def get_riesgo(self):
            return self.riesgo

        def get_descripcion_riesgo(self):
            return self.__descripcion

        def __str__(self):
            cad = self.__nombre + ' '
            cad += self.__apellido + '\t -> '
            cad += str(self.riesgo) + '-' + self.__descripcion
            return cad
        
        def __gt__(self,paciente):
            return self.riesgo > paciente.get_riesgo()
        
if __name__ == "__main__":
    pac1 = Paciente()
    pac2 = Paciente()
    print(pac1>pac2)  
        