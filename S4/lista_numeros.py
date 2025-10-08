from collections import Counter

def pedir_lista_numeros():
    while True:
        entrada = input("Introduce una lista de números separados por comas: ")
        try:
            numeros = []
            for x in entrada.split(","):
                numero = float(x.strip())
                numeros.append(numero)
            return numeros
        except ValueError:
            print("❌ Error: Asegúrate de introducir solo números separados por comas.\n")


def calcular_estadisticas(numeros):
    suma = sum(numeros)
    media = suma / len(numeros)
    maximo = max(numeros)
    
    # Detectar duplicados usando Counter
    contador = Counter(numeros)
    duplicados = [num for num, count in contador.items() if count > 1]
    
    return suma, media, maximo, duplicados


def main():
    numeros = pedir_lista_numeros()
    suma, media, maximo, duplicados = calcular_estadisticas(numeros)

    print("\n📊 Resultados:")
    print(f"Suma: {suma}")
    print(f"Media: {media}")
    print(f"Máximo: {maximo}")
    if duplicados:
        print(f"Duplicados: {duplicados}")
    else:
        print("No hay números duplicados.")


if __name__ == "__main__":
    main()
