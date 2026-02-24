import random

num = random.randint(1, 100)
intentos = 1
while intentos <= 10:
	num_user = int(input('Adivina El Numero: '))
	if num == num_user:
		print('Bien!, Lo Encontraste!')
		print('En', intentos, 'Intentos')
		break
	elif num_user < num:
		print("Uno Mayor")
	else:
		print("Uno Menor")
	intentos += 1

if intentos > 10:
	print("Perdiste")	