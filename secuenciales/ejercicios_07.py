# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a 
# cuantas horas y minutos corresponde.

minutos = int(input('Ingresa la cantidad de minutos : '))

minutitos = minutos // 60
minutin = minutos % 60

print(minutitos, "En horas y ",minutin, "en minutos" )
