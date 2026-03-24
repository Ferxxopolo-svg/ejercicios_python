horas_acum = 0

trabajadores = int(input("¿Cuántos trabajadores tiene la empresa?: "))
sueldo_por_hora = float(input("Sueldo por hora: "))

for trabajador in range(1, trabajadores + 1):
    horas_por_trabajador = 0
    
    dias = int(input(f"¿Cuántos días ha trabajado el trabajador {trabajador}? "))
    
    
    for dia in range(1, dias + 1):
        horas = int(input(f"¿Cuántas horas ha trabajado el trabajador {trabajador} el día {dia}?: "))
        horas_por_trabajador += horas
    
    print(f"El trabajador {trabajador} tiene de sueldo {horas_por_trabajador * sueldo_por_hora}")
    
    horas_acum += horas_por_trabajador

print(f"El pago a los {trabajadores} trabajadores es: {horas_acum * sueldo_por_hora}")