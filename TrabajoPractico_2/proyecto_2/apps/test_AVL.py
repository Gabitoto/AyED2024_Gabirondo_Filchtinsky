# Aplicación secundaria para probar el funcionamiento de las rotaciones en un Arbol AVL

from modules.Temperaturas_DB  import Temperaturas_DB


def imprimir_arbol(nodo, nivel=0, prefijo="Raíz: "):
    """Función para imprimir el árbol de forma visual"""
    if nodo is not None:
        print("  " * nivel + prefijo + f"{nodo.clave} (T: {nodo.valor}°C)")
        if nodo.tieneHijoIzquierdo():
            imprimir_arbol(nodo.hijoIzquierdo, nivel + 1, "L── ")
        if nodo.tieneHijoDerecho():
            imprimir_arbol(nodo.hijoDerecho, nivel + 1, "R── ")

def test_avl():
    print("=== Prueba del Árbol AVL con Base de Datos de Temperaturas ===")
    db = Temperaturas_DB()
    
    while True:
        print("\nMenú de Pruebas:")
        print("1. Insertar temperatura (provoca rotaciones si es necesario)")
        print("2. Mostrar árbol actual")
        print("3. Buscar temperatura por fecha")
        print("4. Eliminar temperatura")
        print("5. Mostrar temperaturas en rango")
        print("6. Ejecutar caso de prueba de rotaciones")
        print("7. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            fecha = input("Ingrese la fecha (formato DD/MM/YYYY): ")
            try:
                temp = float(input("Ingrese la temperatura en °C: "))
                db.guardar_temperatura(fecha, temp)
                print("\nÁrbol después de la inserción:")
                imprimir_arbol(db.base_de_datos.raiz)
            except ValueError:
                print("Error: Ingrese una temperatura válida")
                
        elif opcion == "2":
            print("\nEstado actual del árbol:")
            imprimir_arbol(db.base_de_datos.raiz)
            
        elif opcion == "3":
            fecha = input("Ingrese la fecha a buscar (DD/MM/YYYY): ")
            temp = db.devolver_temperatura(fecha)
            if temp is not None:
                print(f"Temperatura encontrada: {temp}°C")
            
            else:
                print("Fecha no encontrada en el árbol")
                
        elif opcion == "4":
            fecha = input("Ingrese la fecha a eliminar (DD/MM/YYYY): ")
            try:
                db.borrar_temperatura(fecha)
                print("\nÁrbol después de la eliminación:")
                imprimir_arbol(db.base_de_datos.raiz)
            except KeyError:
                print("Error: Fecha no encontrada en el árbol")
                
        elif opcion == "5":
            fecha1 = input("Ingrese fecha inicial (DD/MM/YYYY): ")
            fecha2 = input("Ingrese fecha final (DD/MM/YYYY): ")
            temperaturas = db.devolver_temperaturas(fecha1, fecha2)
            print("\nTemperaturas en el rango especificado:")
            for fecha, temp in temperaturas:
                print(f"{fecha}: {temp}°C")
                
        elif opcion == "6":
            print("\nEjecutando caso de prueba que provoca rotaciones...")
            # Caso que provocará rotaciones
            fechas_temps = [
                ("01/01/2024", 20.0),  # Raíz
                ("02/01/2024", 15.0),  # Provocará rotación simple
                ("03/01/2024", 10.0),  # Provocará rotación simple
                ("01/02/2024", 25.0),  # Balanceará el árbol
                ("02/02/2024", 23.0),  # Provocará rotación doble
            ]
            
            print("\nInsertando datos en secuencia para mostrar rotaciones:")
            for fecha, temp in fechas_temps:
                print(f"\nInsertando: Fecha {fecha}, Temperatura {temp}°C")
                db.guardar_temperatura(fecha, temp)
                print("\nEstado del árbol después de la inserción:")
                imprimir_arbol(db.base_de_datos.raiz)
                
        elif opcion == "7":
            print("¡Hasta luego!")
            break
            
        else:
            print("Opción no válida")

if __name__ == "__main__":
    test_avl()

