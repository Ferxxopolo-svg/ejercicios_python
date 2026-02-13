sueldo_base = float(input("Dime el sueldo base: "))

venta1 = float(input("Dime precio de la venta 1: "))

venta2 = float(input("Dime precio de la venta 2: "))

venta3 = float(input("Dime precio de la venta 3: "))

comision = (venta1 + venta2 + venta3) * 0.10

sueldo_total = sueldo_base + comision

print(f"\nComisión por ventas: ${comision:.2f}")

print(f"Sueldo total: ${sueldo_total:.2f}")