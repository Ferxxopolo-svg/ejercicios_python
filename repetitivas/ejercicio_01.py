print("Programa de factorial de un numero")
numero = int(input("Ingresa un numero: "))

i = 1

factorial = 1
while i <= numero:
	factorial = factorial * i
	i = i + 1
print("El factorial de ",  numero, "Es" , factorial)