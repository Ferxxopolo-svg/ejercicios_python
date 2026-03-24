cad = input("Introduce una cadena: ")

cont = 0
posicion = 0
n = len(cad)

# Saltar espacios iniciales
while posicion < n and cad[posicion] == " ":
    posicion += 1

# Recorrer la cadena
while posicion < n:
    if cad[posicion] == " ":
        cont += 1
        
        while posicion < n and cad[posicion] == " ":
            posicion += 1
    else:
        posicion += 1

if n > 0 and cad[-1] != " ":
    cont += 1

print("La frase tiene", cont, "palabras.")