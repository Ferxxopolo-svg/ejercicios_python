cad = input("Introduce una cadena: ")

while True:
    car = input("Introduce un carácter: ")
    if len(car) == 1:
        break

cont = 0

for posicion in range(len(cad)):
    if cad[posicion] == car:
        cont += 1

print("En la cadena", cad, "aparecen", cont, "veces el carácter", car, ".")