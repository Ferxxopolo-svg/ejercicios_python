def es_bisiesto(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def dias_del_mes(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if es_bisiesto(year) else 28
    else:
        return 0

def validar_fecha(day, month, year):
    if day < 1 or day > dias_del_mes(month, year):
        return False
    return True

def calcular_dia_juliano(day, month, year):
    diaj = 0
    for mes in range(1, month):
        diaj += dias_del_mes(mes, year)
    diaj += day
    return diaj

def leer_fecha():
    while True:
        day = int(input("Día: "))
        month = int(input("Mes: "))
        year = int(input("Año: "))
        
        if validar_fecha(day, month, year):
            return day, month, year
        else:
            print("Fecha no válida")

d, m, a = leer_fecha()

print("Día Juliano:", calcular_dia_juliano(d, m, a))