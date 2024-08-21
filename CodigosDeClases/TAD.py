# Ejemplos de recursion

# Factorial

def factorial(n):
    # En esta funcion aplicamos recursion para poder resolver el factorial de un numero.
    if n>1:
        n = n * factorial(n-1)
        return n
    elif n == 1 or n == 0:
        return 1
    else:
        raise ValueError("Este es un valor incorrecto")
    
objeto = factorial(5)
print(objeto)

# Serie Fibonacci: Este enfoque es más intuitivo, pero tiene una complejidad de tiempo exponencial, lo que significa que se vuelve ineficiente para valores grandes de N.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n = fibonacci(n-1) + fibonacci(n-2)
        return n

for i in range(10):
    print(fibonacci(i), end=" ")
    
# Memoizacion: La memoización es una técnica de optimización utilizada principalmente en programación dinámica y algoritmos recursivos para mejorar la eficiencia de las funciones que calculan resultados repetidos.

def Fibonacci_memo(n, memo={}):
    """Cuando una función recursiva se llama con los mismos argumentos múltiples veces, la memoización guarda los resultados de estas llamadas en una estructura de datos (como un diccionario en Python). En lugar de recalcular el resultado cada vez, la función simplemente devuelve el valor almacenado en el diccionario si ya se ha calculado anteriormente."""
    if n in memo:
        return memo[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = Fibonacci_memo(n-1, memo) + Fibonacci_memo(n -2, memo)
        return memo[n]
    
print(Fibonacci_memo(10))

# Estructuras de Datos.

"""class Listasimp:
    def __init__(self,inicio,espacio):
        self.inicio = None
        self.espacio = None
    
    def agregar(self,n):
        pass"""
        