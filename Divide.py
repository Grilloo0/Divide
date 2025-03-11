def divide(a, b):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if b == 0:
        return "Error: División por 0 no permitida"

    negative = (a < 0) != (b < 0)  
    a, b = abs(a), abs(b)  

    quotient = 0
    while a >= b:
        temp, multiple = b, 1
        while a >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        a -= temp  
        quotient += multiple  

    quotient = -quotient if negative else quotient  
    return max(INT_MIN, min(INT_MAX, quotient))  

# Interfaz del usuario
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
