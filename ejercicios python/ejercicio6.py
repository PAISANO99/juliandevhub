# Calculadora simple con operaciones básicas
x = float(input("Ingresa el primer número: "))
y = float(input("Ingresa el segundo número: "))

print("Suma:", x + y)
print("Resta:", x - y)
print("Multiplicación:", x * y)
if y != 0:
    print("División:", x / y)
else:
    print("No se puede dividir por cero.")
