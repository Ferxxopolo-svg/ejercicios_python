base = int(input("Dime la base: "))
exponente = int(input("Dime el exponente: "))

if exponente > 0:
    potencia = base ** exponente
    print(f"La potencia es {potencia}")
    
elif exponente == 0:
    print("La potencia es 1")
    
else:
    potencia = 1 / (base ** abs(exponente))
    print(f"La potencia es {potencia}")