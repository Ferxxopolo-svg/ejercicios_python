notas = [0] * 5

tam_notas = 5
suma = 0

for indice in range(tam_notas):
    while True:
        try:
            nota = int(input(f"Introduce la nota {indice + 1}: "))
            if 0 <= nota <= 10:
                notas[indice] = nota
                break
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Debes introducir un número válido.")

nota_max = notas[0]
nota_min = notas[0]

for indice in range(tam_notas):
    suma += notas[indice]
    
    if notas[indice] > nota_max:
        nota_max = notas[indice]
        
    if notas[indice] < nota_min:
        nota_min = notas[indice]
nota_media = suma / tam_notas

print("\nNotas:", end=" ")
for indice in range(tam_notas):
    print(notas[indice], end=" ")

print("\nNota media:", nota_media)
print("Nota máxima:", nota_max)
print("Nota mínima:", nota_min)