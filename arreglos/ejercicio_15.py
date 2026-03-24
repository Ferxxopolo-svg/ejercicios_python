num_equipos = 15

equipos = [["", ""] for _ in range(num_equipos)]
resultados = [[0, 0] for _ in range(num_equipos)]

for indice in range(num_equipos):
    equipos[indice][0] = input(f"Introduce el nombre del equipo 1 del partido {indice+1}: ")
    equipos[indice][1] = input(f"Introduce el nombre del equipo 2 del partido {indice+1}: ")
    
    resultados[indice][0] = int(input(f"Introduce los goles metidos por {equipos[indice][0]}: "))
    resultados[indice][1] = int(input(f"Introduce los goles metidos por {equipos[indice][1]}: "))

print("QUINIELA")
print("========")

for indice in range(num_equipos):
    if resultados[indice][0] > resultados[indice][1]:
        signo = "1"
    elif resultados[indice][0] < resultados[indice][1]:
        signo = "2"
    else:
        signo = "X"
    
    print(f"{equipos[indice][0]} - {equipos[indice][1]} -> {signo}")