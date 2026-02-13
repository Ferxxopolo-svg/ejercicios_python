parcial1 = float(input("Dime la nota del parcial 1: "))
parcial2 = float(input("Dime la nota del parcial 2: "))
parcial3 = float(input("Dime la nota del parcial 3: "))
examen = float(input("Dime la nota del examen: "))
trabajo = float(input("Dime la nota del trabajo: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

nota_final = (promedio_parciales * 0.55) + (examen * 0.30) + (trabajo * 0.15)

print(f"\nNota final: {nota_final:.2f}")