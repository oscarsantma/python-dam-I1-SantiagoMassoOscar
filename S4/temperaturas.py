def convertir_temperatura():
    while True:
        try:
            # Pedir la temperatura en grados Celsius
            celsius = float(input("Introduce la temperatura en grados Celsius: "))
            break
        except ValueError:
            print("❌ Error: introduce un número válido.\n")

    while True:
        print("\nElige la unidad a la que deseas convertir:")
        print("1. Kelvin")
        print("2. Fahrenheit")
        opcion = input("Opción (1 o 2): ")

        if opcion == "1":
            kelvin = celsius + 273.15
            print(f"\n🌡️ {celsius} °C son {kelvin} K")
            break
        elif opcion == "2":
            fahrenheit = (celsius * 9/5) + 32
            print(f"\n🌡️ {celsius} °C son {fahrenheit} °F")
            break
        else:
            print("⚠️ Opción no válida. Inténtalo de nuevo.\n")


if __name__ == "__main__":
    convertir_temperatura()
