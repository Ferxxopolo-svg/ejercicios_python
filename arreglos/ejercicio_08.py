tam_vector = 30

nombre = [""] * tam_vector
edad = [0] * tam_vector

indice = 0

while True:
    nombre[indice] = input("Dime el nombre de un alumno: ")
    
    if nombre[indice] != "*":
        edad[indice] = int(input("Dime su edad: "))
    
    indice += 1
    
    if nombre[indice - 1] == "*" or indice == tam_vector:
        break

indice = 0
edad_max = edad[0]

while indice < tam_vector and nombre[indice] != "*":
    if edad[indice] > edad_max:
        edad_max = edad[indice]
    indice += 1

indice = 0
print("Alumnos mayores de edad")
print("=======================")

while indice < tam_vector and nombre[indice] != "*":
    if edad[indice] >= 18:
        print(nombre[indice])
    indice += 1

indice = 0
print("Alumnos mayores")
print("===============")

while indice < tam_vector and nombre[indice] != "*":
    if edad[indice] == edad_max:
        print(nombre[indice])
    indice += 1