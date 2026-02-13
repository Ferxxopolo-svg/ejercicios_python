horapartida = int(input("Hora de salida: "))
minpartida = int(input("Minutos de salida: "))
segpartida = int(input("Segundos de salida: "))
segviaje = int(input("Tiempo que has tardado en segundos: "))

seginicial = horapartida * 3600 + minpartida * 60 + segpartida
segfinal = seginicial + segviaje

horallegada = segfinal // 3600


seg_restantes = segfinal % 3600
minllegada = seg_restantes // 60
segllegada = seg_restantes % 60

print("\nHora de llegada:")
print(f"{horallegada}:{minllegada}:{segllegada}")