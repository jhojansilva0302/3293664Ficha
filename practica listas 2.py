lista1 = [ "manzana", "banana", "cereza", "naranja", "kiwi", "melon", "mango", "pera", "uva", "fresa" ]
lista1.append("mora")
lista2 = [lista1[0], lista1[2], lista1[4]]
print(lista2)
lista1[1] = "piña"
print(lista1)

# Pedir número para lista1
while True:
    try:
        numero1 = int(input("Ingrese un número del 0 al 10: "))
        if 0 <= numero1 <= 10:
            break
        else:
            print("Número fuera de rango, intente de nuevo.")
    except ValueError:
        print("Entrada inválida, debe ser un número.")
print("Número válido:", numero1)
print("La fruta en esa posición es:", lista1[numero1])

# Pedir número para lista2
while True:
    try:
        numero2 = int(input("Ingrese un número del 0 al 2 para la lista2: "))
        if 0 <= numero2 <= 2:
            break
        else:
            print("Número fuera de rango, intente de nuevo.")
    except ValueError:
        print("Entrada inválida, debe ser un número.")
print("Número válido:", numero2)
print("La fruta en esa posición de lista2 es:", lista2[numero2])

# Operaciones
print("¿Qué operación desea realizar con los números ingresados?")
print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Promedio")
opcion = input("Ingrese el número de la opción: ")

if opcion == "1":
    print("Suma:", numero1 + numero2)
elif opcion == "2":
    print("Resta:", numero1 - numero2)
elif opcion == "3":
    print("Multiplicación:", numero1 * numero2)
elif opcion == "4":
    if numero2 != 0:
        print("División:", numero1 / numero2)
    else:
        print("No se puede dividir por cero.")
elif opcion == "5":
    print("Promedio:", (numero1 + numero2) / 2)
else:
    print("Opción no válida.")