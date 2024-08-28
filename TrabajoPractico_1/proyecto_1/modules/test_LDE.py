# Archivo de test para realizar pruebas unitarias del modulo1

# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 14:00:21 2022
@author: Catedra de Algoritmos y Estructura de Datos
"""

from LDE import ListaDobleEnlazada
import unittest
import random


class Test_LDE(unittest.TestCase):
    """Test de la clase ListaDobleEnlazada"""

    def setUp(self):
        self.n_elementos = 200
        """ LDE vacía """
        self.lde_1 = ListaDobleEnlazada()

        """ LDE con elementos repetidos con lista auxiliar"""
        self.lde_2 = ListaDobleEnlazada()
        self.lista_aux_2 = random.choices(range(-self.n_elementos // 2, self.n_elementos // 2), k=self.n_elementos)
        for item in self.lista_aux_2:
            self.lde_2.agregar_al_final(item)

        """LDE de elementos no repetidos con lista auxiliar"""
        self.lde_3 = ListaDobleEnlazada()
        self.lista_aux_3 = random.sample(range(-self.n_elementos, self.n_elementos), self.n_elementos)
        for item in self.lista_aux_3:
            self.lde_3.agregar_al_final(item)

        # self.posicion = random.randint(1, self.n_elementos - 1)  # randint incluye el extremo

    def test_iteracion(self):
        """
        Verificamos que tenga sobrecargado los métodos necesarios para ser
        iterado en un bucle for.
        En cada iteración debe devolver el dato siguiente, no el nodo.
        """

        nodo = self.lde_2.cabeza
        for dato in self.lde_2:
            self.assertEqual(nodo.dato, dato,
                             "Los datos arrojados en el for no coinciden con los datos "
                             "obtenidos por recorrido manual de la LDE desde la cabeza")
            nodo = nodo.siguiente
    
    def test_agregar_al_inicio(self):
        """
        pruebo que al agregar elementos al inicio de la lista
        la misma tiene tamaño correcto y se llena correctamente
        """
        valorNuevo = 25

        # Agregar al inicio de lista no vacia
        lde2_copia = self.lde_2.copiar()
        lde2_copia.agregar_al_inicio(valorNuevo)

        self.recorrer_lista(lde2_copia)
        self.assertEqual(len(self.lde_2), len(lde2_copia) - 1,
                         "El tamaño de la lista luego de agregar debe incrementarse en uno")

        nodo_copia = lde2_copia.cabeza
        self.assertEqual(nodo_copia.dato, valorNuevo,
                         "El primer nodo no contiene el valor que se solicito agregar")

        nodo_copia = nodo_copia.siguiente
        nodo_original = self.lde_2.cabeza
        while nodo_original.siguiente is not None:
            self.assertEqual(nodo_original.dato, nodo_copia.dato,
                             "Se modificaron los datos de la lista luego de agregar el nuevo elemento")
            nodo_original = nodo_original.siguiente
            nodo_copia = nodo_copia.siguiente

        # Anexar en lista vacia (self.lde_1)
        lde1_copia = self.lde_1.copiar()
        lde1_copia.agregar_al_inicio(valorNuevo)

        self.recorrer_lista(lde1_copia)
        self.assertEqual(len(lde1_copia), 1,
                         "Al agregar un elemento al inicio de una lista vacia, su nuevo tamaño debe ser uno")

        self.assertEqual(lde1_copia.cabeza.dato, valorNuevo,
                         "El nodo agregado a la lista vacia no contiene el valor que se solicito agregar")
        self.assertIs(lde1_copia.cabeza, lde1_copia.cola,
                      "En una lista de un elemento, la cabeza es la misma que la cola")

    def test_agregar_al_final(self):
        """
        pruebo que al anexar elementos al final de la lista
        la misma tiene tamaño correcto y se llena correctamente
        """

        valorNuevo = 25

        # Anexar en lista no vacia
        lde2_copia = self.lde_2.copiar()
        lde2_copia.agregar_al_final(valorNuevo)

        self.recorrer_lista(lde2_copia)
        self.assertEqual(len(self.lde_2), len(lde2_copia) - 1,
                         "El tamaño de la lista luego de anexar debe incrementarse en uno")

        nodo_original = self.lde_2.cabeza
        nodo_copia = lde2_copia.cabeza
        while nodo_original.siguiente is not None:
            self.assertEqual(nodo_original.dato, nodo_copia.dato,
                             "Se modificaron los datos de la lista luego de anexar el nuevo elemento")
            nodo_original = nodo_original.siguiente
            nodo_copia = nodo_copia.siguiente

        nodo_copia = nodo_copia.siguiente
        self.assertEqual(nodo_copia.dato, valorNuevo,
                         "El ultimo nodo no contiene el valor que se solicito agregar")
        self.assertIs(nodo_copia, lde2_copia.cola,
                      "El ultimo nodo no coincide con la referencia a la cola de la lista")

        # Anexar en lista vacia (self.lde_1)
        lde1_copia = self.lde_1.copiar()
        lde1_copia.agregar_al_final(valorNuevo)

        self.recorrer_lista(lde1_copia)
        self.assertEqual(len(lde1_copia), 1,
                         "Al anexar un elemento en una lista vacia, su nuevo tamaño debe ser uno")

        self.assertEqual(lde1_copia.cabeza.dato, valorNuevo,
                         "El nodo anexado a la lista vacia no contiene el valor que se solicito agregar")
        self.assertIs(lde1_copia.cabeza, lde1_copia.cola,
                      "En una lista de un elemento, la cabeza es la misma que la cola")
