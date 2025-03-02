def divide(a, b):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if b == 0:
        return "Error: División por 0 no permitida"

    negative = (a < 0) != (b < 0)  # Determina si el resultado es negativo
    a, b = abs(a), abs(b)  # Trabajamos con valores absolutos

    quotient = 0
    while a >= b:
        temp, multiple = b, 1
        while a >= (temp << 1):  # Multiplicamos temp por 2 hasta que sea mayor a a
            temp <<= 1
            multiple <<= 1
        a -= temp  # Restamos el múltiplo más grande posible
        quotient += multiple  # Sumamos cuántas veces restamos

    quotient = -quotient if negative else quotient  # Aplicamos el signo
    return max(INT_MIN, min(INT_MAX, quotient))  # Aseguramos que esté dentro del rango permitido

# Interfaz de usuario
while True:
    print("\nCalculadora de División (sin /, *, %)")
    try:
        num1 = int(input("Ingresa el dividendo: "))
        num2 = int(input("Ingresa el divisor: "))
        print("Resultado:", divide(num1, num2))
    except ValueError:
        print("Error: Ingresa solo números enteros.")
    
    continuar = input("¿Quieres hacer otra división? (s/n): ").lower()
    if continuar != "s":
        print("Saliendo...")
        break