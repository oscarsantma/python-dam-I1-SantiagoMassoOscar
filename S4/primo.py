def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def main():
    try:
        n = int(input("Introduce un número entero: "))
        if es_primo(n):
            print(f"✅ El número {n} es primo.")
        else:
            print(f"❌ El número {n} no es primo.")
    except ValueError:
        print("⚠️ Error: Debes introducir un número entero válido.")


if __name__ == "__main__":
    main()
