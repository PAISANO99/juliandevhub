# Intercambia los valores de dos variables sin usar una variable auxiliar
a = int(input("Ingresa el valor de A: "))
b = int(input("Ingresa el valor de B: "))
a, b = b, a
print("Después del intercambio: A =", a, ", B =", b)
