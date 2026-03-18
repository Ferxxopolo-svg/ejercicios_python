def es_multiplo(num1, num2):
    return num1 % num2 == 0

print("Numero 1: ")
numero1 = int(input())
print("Numero 2: ")
numero2 = int(input())

if es_multiplo(numero1, numero2):
    print(numero1, "Es Multiplo de", numero2)
else:
    print(numero1, "No Es Multiplo de", numero2)