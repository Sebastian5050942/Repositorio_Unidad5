lista = ["La Biblia", "A320 Maintenance", "Exterminator"]
lista2 =[]

lista3 = [123, "Hola", 34.5, "Programación"]
lista4 = []

for libro in lista:
    lista.append(libro + "\n")

archivo = open("libros.txt", "a")
archivo.writelines(lista)
archivo.close()

for dato in lista3:
    lista3.append(str(dato) + "\n")

archivo = open("datos.txt", "a")
archivo.writelines(lista3)
archivo.close()