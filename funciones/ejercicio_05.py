import random

def calcular_max_min(lista):
    vmax = lista[0]
    vmin = lista[0]
    
    for num in lista:
        if num > vmax:
            vmax = num
        if num < vmin:
            vmin = num
    
    return vmax, vmin


size_lista = 10


lista = [random.randint(1, 100) for _ in range(size_lista)]


vmax, vmin = calcular_max_min(lista)


print("Lista:", lista)
print("El valor máximo es", vmax)
print("El valor mínimo es", vmin)