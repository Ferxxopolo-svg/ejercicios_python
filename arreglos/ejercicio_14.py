Precio = [0] * 5
Cantidad = [[0 for _ in range(5)] for _ in range(4)]

for indice_art in range(5):
    Precio[indice_art] = float(input(f"Ingrese Precio Articulo {indice_art+1}: "))


for indice_sucursal in range(4):
    for indice_art in range(5):
        Cantidad[indice_sucursal][indice_art] = float(
            input(f"Ingrese Cant. de Articulo {indice_art+1}, en Sucursal {indice_sucursal+1}: ")
        )

print("Cantidades por artículos:")
for indice_art in range(5):
    suma = (Cantidad[0][indice_art] + Cantidad[1][indice_art] +
            Cantidad[2][indice_art] + Cantidad[3][indice_art])
    print(f"Total articulo {indice_art+1}: {suma}")

Articulos_Sucursal2 = 0
for indice_art in range(5):
    Articulos_Sucursal2 += Cantidad[1][indice_art]

print("Total Sucursal 2:", Articulos_Sucursal2)

print("Sucursal 1, Articulo 3:", Cantidad[0][2])


MayorRec = 0
NumMayor = 0
TotalEmpresa = 0

for indice_sucursal in range(4):
    TotalSucursal = 0
    
    for indice_art in range(5):
        TotalSucursal += Cantidad[indice_sucursal][indice_art] * Precio[indice_art]
    
    print(f"Recaudaciones Sucursal {indice_sucursal+1}: {TotalSucursal}")
    
    
    if TotalSucursal > MayorRec:
        MayorRec = TotalSucursal
        NumMayor = indice_sucursal + 1
    
    TotalEmpresa += TotalSucursal

print("Recaudación total de la empresa:", TotalEmpresa)
print("Sucursal de Mayor Recaudación:", NumMayor)