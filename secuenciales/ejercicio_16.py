v1 = float(input("Dime la velocidad del coche 1 (km/h): "))
v2 = float(input("Dime la velocidad del coche 2 (más pequeña) (km/h): "))
distancia = float(input("Dime la distancia entre los coches (km): "))

tiempo_horas = distancia / (v1 - v2)

tiempo_minutos = tiempo_horas * 60

print(f"Lo alcanza en {tiempo_minutos:.1f} minutos.")