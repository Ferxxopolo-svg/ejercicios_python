tam_vector = 5

vector1 = [0] * tam_vector
vector2 = [0] * tam_vector
vector3 = [0] * tam_vector

for indice in range(tam_vector):
    vector1[indice] = int(input(f"Introduce el elemento {indice + 1} del vector1: "))

for indice in range(tam_vector):
    vector2[indice] = int(input(f"Introduce el elemento {indice + 1} del vector2: "))

for indice in range(tam_vector):
    vector3[indice] = vector1[indice] + vector2[indice]

print("La suma de los vectores es:")
for indice in range(tam_vector):
    print(vector3[indice], end=" ")