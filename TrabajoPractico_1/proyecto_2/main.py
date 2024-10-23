# Aplicación principal

from modules.LDE import ListaDobleEnlazada
#------------------------------- Llamado a la LDE para probar sus funciones -------------------------------#

dll = ListaDobleEnlazada() # Creamos una LDE
print(dll.esta_vacia()) # Verifivamos si esta vacia (True)
dll.agregar_al_inicio(10) 
dll.agregar_al_inicio(20)
dll.agregar_al_inicio(30)
dll.agregar_al_final(40) # Agregamos 4 nodos
print(dll.esta_vacia()) # Verificamos si ahora esta vacia (False)
dll2 = dll.copiar() # la copiamos
print(len(dll2)) # imprimimos su longitud
print(len(dll)) # la longitud de la copia
dll2.concatenar(dll) # Concatenamos ambas listas
print(len(dll2)) # la imprimimos ya unidas
dll.mostrar() # mostramos 
print()
dll2.mostrar()
ob = dll + dll2 # se suman
print(len(ob)) # se muestra esa suma
dll.limpiar() # la vaciamos
print(dll.esta_vacia()) # verificamos si se vacio