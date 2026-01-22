# calcular el perimetro y area de un rectangulo






print("Calculo de area y perimetro de un rectangulo")
base = input('Ingresa la base: ')
base = int(base)

height = input('ingresa la altura: ')
height = int(height)

area = base * height
perimeter = base + base + height + height

print("area", area)
print("perimetro", perimeter)
