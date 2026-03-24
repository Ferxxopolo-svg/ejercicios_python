tam_conductores_max = 10
nombre = [""] * tam_conductores_max
kms = [[0 for _ in range(8)] for _ in range(tam_conductores_max)]

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

while True:
    num_conductores = int(input("¿Cuántos conductores tiene la empresa?: "))
    if num_conductores > tam_conductores_max:
        print(f"Cómo máximo puedo guardar la información de {tam_conductores_max} conductores")
    else:
        break

for indice_cond in range(num_conductores):
    nombre[indice_cond] = input(f"Nombre del conductor {indice_cond+1}: ")
    
    for indice_dias in range(7):
        kms[indice_cond][indice_dias] = int(
            input(f"¿Cuántos km ha realizado el {dias[indice_dias]}?: ")
        )

for indice_cond in range(num_conductores):
    kms[indice_cond][7] = 0
    for indice_dias in range(7):
        kms[indice_cond][7] += kms[indice_cond][indice_dias]

for indice_cond in range(num_conductores):
    print(f"{nombre[indice_cond]} ha realizado {kms[indice_cond][7]} kms.")