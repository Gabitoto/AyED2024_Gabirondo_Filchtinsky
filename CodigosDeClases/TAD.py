# Ejemplos de recursion

# Factorial

def factorial(n):
    # En esta funcion aplicamos recursion para poder resolver el factoria lde un numero.
    if n>1:
        n = n * factorial(n-1)
        return n
    elif n == 1 or n == 0:
        return 1
    else:
        raise ValueError("Este es un valor incorrecto")
    
objeto = factorial(5)
print(objeto)