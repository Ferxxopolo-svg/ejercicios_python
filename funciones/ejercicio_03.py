def tmedia (temp1, temp2):
    return (temp1 + temp2) / 2

print("¿Cuantas Temperaturas vas a calcular?: ")
cantidad = int(input())
for indice in range(cantidad):
    print("introduce temperatura minima: ")
    tmin = float(input())
    print("Introduce temperatura maxima: ")
    tmax = float(input())
    print("Temperatura media: ", tmedia(tmin,tmax))