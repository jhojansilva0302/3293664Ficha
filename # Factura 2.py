# Factura de compra sencilla en Python con listas y for

from datetime import datetime

# Encabezado de la factura
print("="*45)
print("             FACTURA DE COMPRA")
print("="*45)
cliente = input("Nombre del cliente: ")
fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(f"Fecha: {fecha}\n")

# Listas
productos = []     # nombres de productos
cantidades = []    # cantidades
precios = []       # precios unitarios
ivas = []          # iva por cada producto
subtotales = []    # subtotal sin iva
totales = []       # total con iva incluido

while True:
    nombre = input("Nombre del producto (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio unitario: $"))
    iva = precio * 0.19   # IVA del 19%

    # Guardar en listas
    productos.append(nombre)
    cantidades.append(cantidad)
    precios.append(precio)
    ivas.append(iva)
    subtotal = cantidad * precio
    subtotales.append(subtotal)
    totales.append(subtotal + (iva * cantidad))

    print("Producto agregado!\n")

# Mostrar factura
print("\n" + "="*60)
print(f"Cliente: {cliente}")
print(f"Fecha:   {fecha}")
print("="*60)
print("{:<12} {:<10} {:<10} {:<10} {:<10}".format("Producto", "Cantidad", "Precio", "IVA", "Total"))
print("-"*60)

total_general = 0

for i in range(len(productos)):
    print("{:<12} {:<10} {:<10.2f} {:<10.2f} {:<10.2f}".format(
        productos[i], cantidades[i], precios[i], ivas[i], totales[i]))
    total_general += totales[i]

print("-"*60)
print(f"{'TOTAL A PAGAR':<45} ${total_general:.2f}")
print("="*60)
print("Gracias por su compra!")
