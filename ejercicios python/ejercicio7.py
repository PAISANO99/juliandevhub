# Calcula edad en meses y días
edad = int(input("Ingresa tu edad en años: "))
meses = edad * 12
dias = edad * 365  # Aproximación sin contar años bisiestos
print("Tienes aproximadamente", meses, "meses y", dias, "días.")
