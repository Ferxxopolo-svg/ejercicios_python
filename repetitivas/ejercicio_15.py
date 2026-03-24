pago_acum = 0
pago = 10

for mes in range(1, 21):
    pago_acum += pago
    pago *= 2

print("Al final de los 20 meses tuvo que pagar:", pago_acum)