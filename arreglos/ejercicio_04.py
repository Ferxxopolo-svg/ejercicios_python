vector = [0] * 10

tam_vector = 10
indice = 0

while True:
    num = int(input(f"Introduce un número en el vector. Número {indice + 1}: "))
    vector[indice] = num
    indice += 1
    
    if indice == tam_vector or num < 0:
        break

indice = 0
print("Elementos del vector:", end=" ")

while indice < tam_vector and vector[indice] >= 0:
    print(vector[indice], end=" ")
    indice += 1