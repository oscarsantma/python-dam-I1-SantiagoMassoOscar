# eco_io.py

# Pedir 3 números por pantalla
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Calcular suma, media y mayor
suma = num1 + num2 + num3
media = suma / 3
mayor = max(num1, num2, num3)

# Mostrar resultados
print(f"Suma: {suma}")
print(f"Media: {media}")
print(f"Mayor: {mayor}")

# Evaluar resultado de la media
if media > 10:
    print("Sobresaliente")
elif media >= 5:
    print("Aprobado")
else:
    print("Suspenso")
