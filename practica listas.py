
lista1 = [ "manzana", "banana", "cereza", "naranja", "kiwi", "melon", "mango", "pera", "uva", "fresa" ]
lista1.append("mora")
lista2 = [lista1 [0], lista1[2], lista1[4],]
print(lista1[5], lista1[1])
print(lista1[::-1]) 
print(lista1[1], lista1[3], lista1[7])  
print(lista2)
lista1[1] = "piña"

while True:
    try:
        numero = int(input("Ingrese un número del 0 al 10: "))
        if 0 <= numero <= 10:
            break
        else:
            print("Número fuera de rango, intente de nuevo.")
    except ValueError:
        print("Entrada inválida, debe ser un número.")
print("Número válido:", numero)
print("La fruta en esa posición es:", lista1[numero])       