import random

numeros = []

for i in range(10):
    numeros.append(random.randint(1, 10))

for n in numeros:
    print("Numero: ", n)
    print("Cuadrado: ", n ** 2)
    print("Cubo: ", n ** 3)