cant_dias = 5
temperatura = [[0, 0] for _ in range(cant_dias)]

for indice in range(cant_dias):
    temperatura[indice][0] = float(input(f"Día {indice+1}. Temperatura mínima: "))
    temperatura[indice][1] = float(input(f"Día {indice+1}. Temperatura máxima: "))

print("Temperaturas medias")
print("===================")
for indice in range(cant_dias):
    media = (temperatura[indice][0] + temperatura[indice][1]) / 2
    print(f"Día {indice+1}. Temperatura media: {media}")

temp_min = temperatura[0][0]
for indice in range(cant_dias):
    if temperatura[indice][0] < temp_min:
        temp_min = temperatura[indice][0]

print("Días con menos temperatura")
print("==========================")
for indice in range(cant_dias):
    if temperatura[indice][0] == temp_min:
        print(f"Día {indice+1}")

existe_temperatura = False
print("Días con temperatura máxima")
print("===========================")
temp_max = float(input("Introduce una temperatura: "))

for indice in range(cant_dias):
    if temperatura[indice][1] == temp_max:
        print(f"Día {indice+1}")
        existe_temperatura = True

if not existe_temperatura:
    print("No hay ningún día con dicha temperatura.")