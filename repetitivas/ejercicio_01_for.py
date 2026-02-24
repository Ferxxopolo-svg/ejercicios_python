#Programa para calcular el factorial de un no se que

num = int(input("Ingresa Un Numero: "))

factorial = 1
for i in range(num): #[0 , 1, 2, 3]
	factorial *= (i + 1)

print('El factorial de ', num, 'Es:', factorial)