num_filas = 5
num_cols = 5

matriz = [[0 for _ in range(num_cols)] for _ in range(num_filas)]

for fila in range(num_filas):
    for col in range(num_cols):
        if fila == col or fila == (num_filas - 1) - col:
            matriz[fila][col] = 1
        else:
            matriz[fila][col] = 0

for fila in range(num_filas):
    for col in range(num_cols):
        print(matriz[fila][col], end=" ")
    print()