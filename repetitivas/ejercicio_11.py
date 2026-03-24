import math

es_primo = True

numero_es_primo = int(input("Introduce un número para comprobar si es primo: "))

if numero_es_primo < 2:
    es_primo = False
else:
    for num in range(2, int(math.sqrt(numero_es_primo)) + 1):
        if numero_es_primo % num == 0:
            es_primo = False

if es_primo:
    print("Es Primo")
else:
    print("No es Primo")