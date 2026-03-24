num_filas = 5
num_cols = 15

matriz = [[0 for _ in range(num_cols)] for _ in range(num_filas)]

for fila in range(num_filas):
    for col in range(num_cols):
        if fila == 0 or fila == num_filas - 1 or col == 0 or col == num_cols - 1:
            matriz[fila][col] = 1
        else:
            matriz[fila][col] = 0

for fila in range(num_filas):
    for col in range(num_cols):
        print(matriz[fila][col], end=" ")
    print()