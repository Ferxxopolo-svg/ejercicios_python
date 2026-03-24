ahorro_acum = 0

for mes in range(1, 13):
    cant_mensual = float(input(f"¿Cuánto has ahorrado en el mes {mes}?: "))
    ahorro_acum += cant_mensual
    print(f"En el mes {mes} llevas ahorrado {ahorro_acum}")