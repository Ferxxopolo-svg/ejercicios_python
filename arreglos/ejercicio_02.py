vector1 = [""] * 5
vector2 = [""] * 5

tam_vector1 = 5
tam_vector2 = 5

for indicador1 in range(tam_vector1):
    vector1[indicador1] = input(f"Dame la cadena {indicador1 + 1}: ")
indicador2 = 0
for indicador1 in range(tam_vector1 - 1, -1, -1):
    vector2[indicador2] = vector1[indicador1]
    indicador2 += 1
for indicador2 in range(tam_vector2):
    print(f"La cadena {indicador2 + 1}: {vector2[indicador2]}")