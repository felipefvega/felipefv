try:
    # Intentamos dividir dos números
    resultado = 10 / 0
    print("El resultado es:", resultado)
except ZeroDivisionError:
    # Si ocurre un error de división por cero, este bloque se ejecuta
    print("¡No se puede dividir por cero!")
