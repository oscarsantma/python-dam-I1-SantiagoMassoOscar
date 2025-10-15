def main():
    # Pedimos al usuario que ingrese una lista de calificaciones separadas por comas
    entrada = input("Introduce una lista de calificaciones separadas por comas (ejemplo: 6.5, 8, 5, 4, 9, 10, 7, 3): ")

    # Convertimos la entrada en una lista de strings, separando por coma
    notas_str = entrada.split(',')

    # Creamos una lista para almacenar las notas ya convertidas a float
    notas = []

    # Validamos que cada valor sea numérico y lo convertimos a float
    for nota in notas_str:
        try:
            # Quitamos espacios y convertimos a float
            num = float(nota.strip())
            notas.append(num)
        except ValueError:
            print(f"Error: '{nota.strip()}' no es un número válido.")
            return

    total_notas = len(notas)
    media = round(sum(notas) / total_notas, 2)
    minima = min(notas)
    maxima = max(notas)

    aprobados = len([n for n in notas if n >= 5])
    porc_aprobados = (aprobados / total_notas) * 100

    sobresalientes = len([n for n in notas if n >= 9])
    porc_sobresalientes = (sobresalientes / total_notas) * 100

    # Cálculo de la moda sin usar Counter
    modas = []
    max_frecuencia = 0

    for nota in notas:
        frecuencia = notas.count(nota)  # Cuenta cuántas veces aparece esta nota
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia
            modas = [nota]
        elif frecuencia == max_frecuencia and nota not in modas:
            modas.append(nota)

    if media >= 8:
        mensaje = "Nivel excelente"
    elif 5 <= media < 8:
        mensaje = "Nivel medio"
    else:
        mensaje = "Necesita refuerzo"

    print("\n--- Resumen Estadístico ---")
    print(f"Número total de notas: {total_notas}")
    print(f"Media: {media}")
    print(f"Nota mínima: {minima}")
    print(f"Nota máxima: {maxima}")
    print(f"Porcentaje de aprobados (≥5): {porc_aprobados:.2f}%")
    print(f"Porcentaje de sobresalientes (≥9): {porc_sobresalientes:.2f}%")

    if len(modas) == 1:
        print(f"Nota más repetida (moda): {modas[0]}")
    else:
        modas_str = ", ".join(str(m) for m in modas)
        print(f"Notas más repetidas (moda): {modas_str}")

    print(f"Mensaje final: {mensaje}")

if __name__ == "__main__":
    main()