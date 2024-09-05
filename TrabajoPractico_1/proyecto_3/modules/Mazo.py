

from Carta import Carta
from LDE import ListaDobleEnlazada

class DequeEmptyError(Exception):
    """Un jugador se ha quedado sin cartas"""
    def __init__(self,message = "Un jugador se ha quedado sin cartas"):
        self.massage = message

class Mazo():
    def __init__ (self):
        self.mazo = ListaDobleEnlazada()
        
    def poner_carta_arriba(self, carta):
        self.mazo.agregar_al_inicio(carta)
        self.cabeza = carta
            
    def poner_carta_abajo(self,carta):
        carta.visible = False
        self.mazo.agregar_al_final(carta)
        self.cola = carta
    
    def sacar_carta_arriba(self):
        if self.mazo.tamanio > 0 and self.mazo.cabeza is not None:
            carta = self.mazo.extraer(0)
            carta.visible = True
            return carta
        else:   
            raise DequeEmptyError
        
        
    def __len__ (self):
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
