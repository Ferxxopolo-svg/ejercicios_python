while True:
	while True:
		car = input('Introduce Un Caracter: ')
		if len(car) == 1:
			break
		else:
			print("Debes Introducir solo un caracter")
	if car == " ":
		break
	car = car.upper()
	if car in ["A", "E", "I", "O", "U"]:
		print("Vocal")
	else:
		print("No Vocal")