from modules.Grafo import Grafo
from modules.Prim import prim

with open("aldeas.txt", "r" ) as aldeas:
    pueblos = []
    datos_ciudades = []
    
    for ruta in aldeas:
        ruta = ruta.rstrip()
        de, a, distancia = ruta.split(",")
        datos_ruta = [de, a, int(distancia)]
        datos_ciudades.append(datos_ruta)
        
        if de not in pueblos:
            pueblos.append(de)
        if a not in pueblos:
            pueblos.append(a)

    print(datos_ciudades)


