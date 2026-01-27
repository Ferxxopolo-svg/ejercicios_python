# Condicionales con python

# if, else, elif

"""
if exp_bool:
	instrucciones

if exp_bool:
	instruccciones

else:
	instrucciones

if exp_bool:
	instrucciones

elif expo_bool:
	instrucciones

else:
	instrucciones
"""

print("inicio")

numero = int(input('Ingresa un numero : '))

if	numero > 0:
	
	print('Es un numero positivo')
elif numero == 0:
	print("Es Cero")
else:
	print('No Es Positivo')

print("Fin")