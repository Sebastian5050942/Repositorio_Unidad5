file_name = input("Ingrese el nombre del archivo: ")
frase = input("Ingresa una frase motivadora: ")
user_name = input("Ingresa tu nombre")
age = int(input("Ingresa tu edad"))

file_name = file_name + ".txt"

file = open(file_name, "w")
file.write(f"Nombre de usuario: {user_name}\n")
file.write(f"Edad del usuario {age}\n")
file.write(f"Frase: {frase}\n")
file.close()