

from modules.Carta import Carta  
from modules.LDE import ListaDobleEnlazada

# Explicacion de un DequeEmptyError(Exception) = Es una excepción personalizada que se lanza cuando intentas realizar una operación en un deque (doblemente terminado) vacío, como extraer un elemento cuando no hay ninguno disponible.
class DequeEmptyError(Exception):
    def __init__(self,message = "Un jugador se ha quedado sin cartas"):
        self.massage = message

class Mazo():
    def __init__ (self):
        """Se busca que el mazo actue como una LDE y posea sus metodos y atributos"""
        self.mazo = ListaDobleEnlazada()
        
    def poner_carta_arriba(self, carta):
        """Colocamos una carta al inicio del mazo por lo que se utiliza la funcion del la LDE: Agregar_al_inicio."""
        self.mazo.agregar_al_inicio(carta)
        self.cabeza = carta
            
    def poner_carta_abajo(self,carta):
        """Colocamos una carta abajo del mazo por lo que ademas de agregarla al final debemos setearla para que no sea visible."""
        carta.visible = False
        self.mazo.agregar_al_final(carta)
        self.cola = carta
    
    def sacar_carta_arriba(self):
        """La función primero verifica que el mazo no esté vacío y que la cabeza del mazo no sea None.
        Si estas condiciones se cumplen, crea un objeto Carta,lo marca como visible (ya que se está mostrando) y lo retorna.
        Si no hay más cartas, lanza una excepción."""
        if self.mazo.tamanio > 0 and self.mazo.cabeza is not None:
            carta = self.mazo.extraer(0)
            carta.visible = True
            return carta
        else:   
            raise DequeEmptyError
        
        
    def __len__ (self):
        """Llamamos a la funcion de la LDE que nos permite utilizar el metodo len() sobre nuestro mazo."""
        return self.mazo.__len__()

if __name__ == "__main__":             
    carta = Carta('4', 'treboles')
    carta2 = Carta('5', 'treboles')
    carta3 = Carta('10', 'treboles')
    carta4 = Carta('1', 'treboles')
    mazo = Mazo()
    mazo.poner_carta_arriba(carta)
    mazo.poner_carta_arriba(carta2)
    mazo.poner_carta_arriba(carta3)
    mazo.poner_carta_arriba(carta4)
    carta.visible = True
    print(carta)
    print(len(mazo))
