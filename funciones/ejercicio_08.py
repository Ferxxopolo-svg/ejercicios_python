def calcular_factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero1 = int(input("Número: "))

print("El factorial es:", calcular_factorial(numero1))