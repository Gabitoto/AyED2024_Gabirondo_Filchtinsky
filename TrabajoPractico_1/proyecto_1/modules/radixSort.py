# Radix Sort

def counting_sort_strings(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (int(arr[i]) // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (int(arr[i]) // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    """Este algoritmo comienza por el dígito menos significativo (LSD - Least Significant Digit) o el dígito más significativo (MSD - Most Significant Digit),
    dependiendo de la variante luego agrupa a los números en cubetas (buckets) según el valor del dígito actual después los ordenar por un dígito,
    repite el proceso para el siguiente dígito y una vez procesados todos los dígitos, los números estarán completamente ordenados."""
    max_val = max(arr, key=int)

    exp = 1
    while int(max_val) // exp > 0:
        counting_sort_strings(arr, exp)
        exp *= 10