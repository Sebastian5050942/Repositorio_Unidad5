# Clase 20 de Octubre / 2026

## Código VSC: 

```python
nombre_archivo = input("Nombra a tu nuevo archivo (ej: diario.txt): ")

# Contexto de escritura
# Ejercicio: Leer todo el archivo en este mismo contexto
with open(nombre_archivo, 'w+') as archivo:
    datos = input("Escribe tu primer secreto:")
    archivo.write(datos)
    archivo.seek(0) #Mover puntero del archivo al inicio
    frase = archivo.read()
    print(frase)

# Contexto de lectura
# With open (nombre_archivo, 'r') as archivo:
#      print("\n--- Leyendo tu archivo ---")
#      print(archivo.read())
```

### Prueba en la Terminal:
<img width="680" height="248" alt="image" src="https://github.com/user-attachments/assets/d51e4598-87ec-4362-bbd4-979fc0843add" />

## Código VSC: 

```python
try:
    numero = int(input("Ingrese un número entero:"))
except ValueError:
    print("El dato ingresado es incorrecto.")
else:

    print(numero)
finally:
    print("Fin de esta parte")
```

### Prueba en la Terminal:
<img width="801" height="330" alt="image" src="https://github.com/user-attachments/assets/1487ca89-4694-48f5-86a5-e9187990c9fe" />

## Código VSC: 

```python
# Código propenso a errores (Si el usuario escribe algo mal, el programa explota)
nombre = input("Dime qué archivo quieres leer: ")

# TODO: Añade el bloque try - except aquí
with open(nombre, "r") as archivo:
    print(archivo.read())

print("Fin del programa. Gracias por usar nuestro sistema.")
```

### Prueba en la Terminal:
<img width="807" height="284" alt="image" src="https://github.com/user-attachments/assets/1b6c7b50-1cad-4e96-9ee4-43d80be2353f" />

## Código VSC: 

```python
# Abrir un archivo usando el modo x

with open("datos.txt", "x") as file:
    texto = file.read()
    print(texto)
```

### Prueba en la Terminal:
<img width="807" height="251" alt="image" src="https://github.com/user-attachments/assets/0f024f46-1117-4e2f-bf92-4dbb706d1ab9" />

## Código VSC: 

```python
import csv

with open("notas.csv","r") as csvfile:
    print(csvfile)
    lector = csv.reader(csvfile, delimiter= ';')
    print(lector)
    encabezado = next
    for dato in lector:
        print(dato)
```

### Prueba en la Terminal:

# Datos Abiertos Colombia
<img width="1913" height="1079" alt="image" src="https://github.com/user-attachments/assets/aafe5d61-91e8-45b1-a06a-9abd8be2a659" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/f2db4791-dbea-44e2-9ac5-3a54844ff55b" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/94b94074-f7fa-425d-91a5-329b527c22f8" />
<img width="1919" height="1070" alt="image" src="https://github.com/user-attachments/assets/f759777f-2261-4d8b-930b-19223185832f" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/f15ba8aa-ea76-4ad9-9550-dad6cacfffa1" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/30200ff4-f5a7-4729-ae24-ebc64417da8b" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/e22f8ae9-38ab-4764-b2e9-8bbe84a86a5a" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/f9624e07-3f6f-4b9b-acf8-17f4e58984ed" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/1d907d74-aeb7-4721-8206-cb386a977378" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/7823b753-1a39-4703-89df-6ef076bda901" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/be8d6e3f-cd7c-4430-8be7-dff456e8c384" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/ab261fb2-cc2e-4476-86dd-43c6f7565d23" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/9de792f5-e68c-4932-b20b-28275ddcc9e5" />






