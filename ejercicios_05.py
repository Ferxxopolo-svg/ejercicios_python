# Escribir un programa que convierta un valor dado en grados

print("Conversacion de fahrenheit a Celsius")
fahrenheit = float(input("Ingresa los grados fahrenheit : "))
celsius = (fahrenheit - 32) * (5 / 9)

print("grados fahrenheit" , fahrenheit)
print("grados Celsius" , celsius)

print(f'{ fahrenheit }°F equivalen {celsius}°C ' )