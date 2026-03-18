def convertir_espaciado(cad):
    nueva_cad = ' '
    for letra in cad:
        nueva_cad += letra + ' '
    return nueva_cad
cadena = input("Introduce una cadena de texto: ")
print(convertir_espaciado(cadena))