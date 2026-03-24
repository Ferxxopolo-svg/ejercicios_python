def convertir_a_segundos(hor, min, seg):
    return hor * 3600 + min * 60 + seg

def convertir_a_hms(segund):
    hor = segund // 3600
    segund %= 3600
    min = segund // 60
    seg = segund % 60
    return hor, min, seg

while True:
    print("1.- Convertir a segundos")
    print("2.- Convertir a horas, minutos y segundos")
    print("3.- Salir")
    
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        hor = int(input("Horas: "))
        min = int(input("Minutos: "))
        seg = int(input("Segundos: "))
        
        total = convertir_a_segundos(hor, min, seg)
        print("Corresponde a", total, "segundos.")
        
    elif opcion == 2:
        segund = int(input("Segundos: "))
        hor, min, seg = convertir_a_hms(segund)
        print(f"Corresponde a {hor}:{min}:{seg}")
        
    elif opcion == 3:
        break
        
    else:
        print("Opción incorrecta")