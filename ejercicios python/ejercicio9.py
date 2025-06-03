# Verifica si un número es múltiplo de otro
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

if b != 0 and a % b == 0:
    print(a, "es múltiplo de", b)
else:
    print(a, "no es múltiplo de", b)
