def analizar_cadena():
    texto = input("Introduce una cadena de texto: ")

    vocales = "aeiouAEIOU"
    contador_vocales = 0
    contador_consonantes = 0
    contador_mayusculas = 0
    total_caracteres = len(texto)

    for caracter in texto:
        if caracter.isalpha():  # Solo letras
            if caracter in vocales:
                contador_vocales += 1
            else:
                contador_consonantes += 1

        if caracter.isupper():
            contador_mayusculas += 1

    print("\n📊 Resultados:")
    print(f"Vocales: {contador_vocales}")
    print(f"Consonantes: {contador_consonantes}")
    print(f"Mayúsculas: {contador_mayusculas}")
    print(f"Número total de caracteres: {total_caracteres}")


if __name__ == "__main__":
    analizar_cadena()
