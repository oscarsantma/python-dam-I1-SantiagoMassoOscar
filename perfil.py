from datetime import datetime

def obtener_edad(anio_nacimiento):
    anio_actual = datetime.now().year
    return anio_actual - anio_nacimiento

def clasificar_edad(edad):
    if edad < 18:
        return "Menor de edad (<18)"
    elif 18 <= edad <= 65:
        return "Adulto (18-65)"
    else:
        return "Mayor de 65 años (>65)"

nombre = input("Introduce tu nombre: ")
anio_nacimiento_str = input("Introduce tu año de nacimiento: ")

if not anio_nacimiento_str.isdigit():
    print("No has introducido un año válido.")
else:
    anio_nacimiento = int(anio_nacimiento_str)
    edad = obtener_edad(anio_nacimiento)
    tramo = clasificar_edad(edad)
    print(f"{nombre}, tienes {edad} años. Clasificación: {tramo}")