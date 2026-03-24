def calcular_factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero1 = int(input("Número: "))

if numero1 < 0:
    print("El factorial no está definido para números negativos")
else:
    print("El factorial es:", calcular_factorial(numero1))