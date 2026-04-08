# 1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while). 
# 2. Pedir cantidad de productos a comprar (número entero positivo, validar con .isdigit() en while). 
# 3. Por cada producto (usar for): 
#   o Pedir precio (entero, validar .isdigit()). 
#   o Pedir si tiene descuento S/N (validar con while, aceptar s o n en cualquier mayuscula/minuscula). 
#   o Si tiene descuento: aplicar 10% al precio de ese producto. 
# 4. Al final mostrar: 
#   o Total sin descuentos 
#   o Total con descuentos 
#   o Ahorro total 
#   o Promedio por producto (usar float y formatear con :.2f, ejem: 
#       x = 3.14159 
#       print(f"{x:.2f}"))
contSinDescuento = 0
contConDescuento = 0
precioTotalSinDescuento = 0
precioTotalConDescuento = 0
ahorroTotal = 0
promedioPorProducto = 0

nombre_cliente = input("Ingrese el nombre del cliente: ")
while not nombre_cliente.isalpha():
    nombre_cliente = input("Ingrese el nombre del cliente: ")

cantidad_productos = input("Ingrese la cantidad de productos a comprar: ")
while not cantidad_productos.isdigit():
    cantidad_productos = input("Ingrese la cantidad de productos a comprar: ")

cantidad_productos = int(cantidad_productos)
for i in range(cantidad_productos):
    precio_producto = input("Ingrese el precio del producto: ")
    while not precio_producto.isdigit():
        precio_producto = input("Nombre invalido. Ingrese el precio del producto: ")
    tiene_descuento = input("Ingrese si tiene descuento S/N: ").strip().upper()
    while tiene_descuento not in ["S", "N"]:
        tiene_descuento = input("Valor invalido. Ingrese si tiene descuento S/N: ").strip().upper()
    if tiene_descuento == "S":
        descuento = float(precio_producto) * 0.1
        precio_producto = float(precio_producto) - descuento
        contConDescuento += 1
        ahorroTotal += descuento
        precioTotalConDescuento += float(precio_producto)
    else:
        contSinDescuento += 1
        precioTotalSinDescuento += float(precio_producto)

promedioPorProducto = (precioTotalSinDescuento + precioTotalConDescuento) / cantidad_productos

print(f"Total sin descuentos: {precioTotalSinDescuento}")
print(f"Total con descuentos: {precioTotalConDescuento}")
print(f"Ahorro total: {ahorroTotal}")
print(f"Promedio por producto: {promedioPorProducto:.2f}")
