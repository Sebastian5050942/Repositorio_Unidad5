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

# RETO Unidad 5

# Codigó VSC:

```python
def explorar_directorio():
    from pathlib import Path
    opcion = 0
    ruta = Path("rutafalsa")
    lista = []
    while opcion != 1 and opcion != 2:
        print("1. Ingresar ruta personalizada\n2. Usar ruta por defecto")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Opción no válida. Intente nuevamente.")
            continue
        if opcion == 1:
            while ruta.exists() == False:
                ruta = Path(input("Ingrese la ruta separando con doble backslash (\\): "))
                if ruta.exists() == False:
                    print("La ruta ingresada no existe. Intente nuevamente.")
            for archivo in ruta.iterdir():
                if archivo.is_file() and archivo.suffix == ".txt" or archivo.suffix == ".csv":
                    lista.append(archivo.name)
            if len(lista) > 0:
                print("Archivos encontrados:")
                for archivo in lista:
                    print(archivo)
            else:
                print("No se encontraron archivos .txt o .csv en la ruta especificada.")
        elif opcion == 2:
            ruta = Path(".\\Reto\\Archivos_Reto")
            for archivo in ruta.iterdir():
                if archivo.is_file() and archivo.suffix == ".txt" or archivo.suffix == ".csv":
                    lista.append(archivo.name)
            if len(lista) > 0:
                print("Archivos encontrados:")
                for archivo in lista:
                    print(archivo)
            else:
                print("No se encontraron archivos .txt o .csv en la ruta especificada.")
        else:
            print("Opción no válida. Intente nuevamente.")

def procesar_bitacoras():
    from pathlib import Path
    from matplotlib import pyplot as plt
    ruta = Path("rutafalsa")
    conectores = ["el", "la", "los", "las", "un", "una", "unos", "unas", "de", "del", "al", "y", "o", "a", "en", "con", "por", "para", "que", "se", "es", "son", "su", "sus"]
    while ruta.exists() == False or ruta.suffix != ".txt":
        print("La ruta ingresada no es válida o el archivo no es un .txt. Intente nuevamente.")
        ruta = Path(input("Ingrese la ruta del archivo de bitácora (separando con doble backslash (\\)): "))
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            cantidad_de_lineas = len(lineas)
        with open(ruta, "r", encoding="utf-8") as archivo:
            texto = archivo.read()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return   
    palabras = texto.split()
    cantidad_de_palabras = len(palabras)
    caracteres_esp = len(texto)
    caracteres = 0
    for caracter in texto:
        if caracter != " " and caracter != "\n":
            caracteres += 1
    frecuencias = {}
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra not in conectores:
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1
    frecuencia_ordenada = []
    for palabra, frecuencia in frecuencias.items():
        frecuencia_ordenada.append((frecuencia, palabra))
    lista_ordenada = sorted(frecuencia_ordenada)
    print(f"RESUMEN ESTADÍSTICO DEL TEXTO: \nCantidad de líneas: {cantidad_de_lineas}\nCantidad de palabras: {cantidad_de_palabras}\nCantidad de caracteres (sin espacios): {caracteres}\nCantidad de caracteres (con espacios): {caracteres_esp}")
    for i in range(5):
        print(f"{i+1}. {lista_ordenada[(-i-1)][1]}: {lista_ordenada[(-i-1)][0]} veces")
    top_palabras = []
    repeticiones = []
    for c in range(10):
        top_palabras.append(lista_ordenada[(-c-1)][1])
        repeticiones.append(lista_ordenada[(-c-1)][0])
    plt.barh(top_palabras, repeticiones)
    plt.xlabel("Frecuencia")
    plt.ylabel("Palabras")
    plt.title("Top 10 Palabras más usadas")
    plt.show()
    longitudes = []
    for linea in lineas:
        longitudes.append(len(linea))
    if len(longitudes) > 0:
        plt.hist(longitudes, bins=range(0, max(longitudes) + 26, 25), edgecolor="black")
        plt.xlabel("Longitud de las líneas")
        plt.ylabel("Frecuencia")
        plt.title("Distribución de la longitud de las líneas")
        plt.show()
def analizar_dataset():
    from matplotlib import pyplot as plt
    from pathlib import Path
    import csv

    ruta = Path("rutafalsa")
    while not ruta.exists() or ruta.suffix.lower() != ".csv":
        print("La ruta ingresada no es válida o el archivo no es un .csv. Intente nuevamente.")
        ruta = Path(input("Ingrese la ruta del archivo de dataset (separando con doble backslash (\\\\)): "))

    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        datos = list(lector)
    if len(datos) == 0:
        print("El archivo CSV está vacío.")
        return

    columnas = list(datos[0].keys())
    print("\nPRIMERAS 10 FILAS:")
    for fila in datos[:10]:
        print(fila)

    print("\nÚLTIMAS 5 FILAS:")
    for fila in datos[-5:]:
        print(fila)

    print("\nCOLUMNAS DISPONIBLES:")
    i = 1
    for columna in columnas:
        print(f"{i}. {columna}")
        i += 1

    try: 
        indice = int(input("\nSeleccione una columna numérica para estadísticas: "))
    except ValueError:
        print("Selección inválida. Debe ingresar un número.")
        return
    
    columna = columnas[(indice) - 1]
    
    valores = []
    for fila in datos:
        valor = fila[columna]
        if valor != "":
            try:
                valores.append(float(valor))
            except ValueError:
                continue

    if len(valores) > 0:
        promedio = sum(valores) / len(valores)
        valores_ordenados = sorted(valores)
        n = len(valores_ordenados)

        if n % 2 == 1:
            mediana = valores_ordenados[n // 2]
        else:
            mediana = (valores_ordenados[n // 2 - 1] + valores_ordenados[n // 2]) / 2

        print(f"""
    ESTADÍSTICAS DE {columna}:
    Total de registros válidos: {len(valores)}
    Promedio: {promedio}
    Mediana: {mediana}
    Máximo: {max(valores)}
    Mínimo: {min(valores)}
    """)
    else:
        print("No hay datos numéricos válidos.")

    print("GRÁFICO DE LÍNEAS")

    try:
        x_i = int(input("Seleccione una columna para el eje X: ")) - 1
        y_i = int(input("Seleccione una columna para el eje Y: ")) - 1
        x_col = columnas[x_i]
        y_col = columnas[y_i]
    except (ValueError, IndexError):
        print("Selección inválida.")
        return

    x = []
    y = []

    for fila in datos:
        try:
            x.append(float(fila[x_col]))
            y.append(float(fila[y_col]))
        except ValueError:
            continue

    if len(y) > 0:
        plt.plot(x, y)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f"Gráfico de líneas: {y_col} vs {x_col}")
        plt.show()
    else:
        print("No hay datos numéricos válidos para graficar.")
    print("GRÁFICO DE PASTEL")
    indice = input("Seleccione una columna categórica para el gráfico de pastel: ")
    indice = int(indice) - 1
    columna = columnas[indice]
    categorias = {}

    for fila in datos:
        valor = fila[columna].strip()
        if valor != "":
            if valor in categorias:
                categorias[valor] += 1
            else:
                categorias[valor] = 1

    print(categorias)
    if len(categorias) > 0:
        etiquetas = []
        cantidades = []
        for categoria in categorias:
            etiquetas.append(categoria)
            cantidades.append(categorias[categoria])
        
        plt.pie(cantidades, labels=etiquetas, autopct="%1.1f%%", startangle=90)
        plt.title(f"Distribución de {columna}")
        plt.axis("equal")
        plt.show()
    else:
        print("No hay datos para el gráfico de pastel.")
    print("GRÁFICO DE DISPERSIÓN")
    x_i = int(input("Seleccione una columna para el eje X del gráfico de dispersión: ")) - 1
    y_i = int(input("Seleccione una columna para el eje Y del gráfico de dispersión: ")) - 1
    x_col = columnas[x_i]
    y_col = columnas[y_i]
    x = []
    y = []
    for fila in datos:
        try:
            x.append(float(fila[x_col]))
            y.append(float(fila[y_col]))
        except ValueError:
            continue
    if len(x) > 0:
        plt.scatter(x, y)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f"Correlación entre {y_col} y {x_col}")
        plt.show()
    else:
        print("No hay datos válidos para el gráfico de dispersión.")
while True:  
    print("BIENVENIDO AL PROGRAMA DE ANÁLISIS DE DATOS\nSeleccione una opción para continuar:\n1. Explorar directorio\n2. Procesar bitácoras\n3. Analizar dataset\n4. Salir")
    try:
        opcion = int(input("Ingrese el número de la opción deseada: "))
    except ValueError:
        print("Opción no válida. Intente nuevamente.")
        continue
    if opcion == 1:
        explorar_directorio()
    elif opcion == 2:
        procesar_bitacoras()
    elif opcion == 3:
        analizar_dataset()
    elif opcion == 4:
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
```

# Link de Video - Sustentación:

https://youtu.be/3F0MJ08m4ts?si=rQefdKJl1uQy1193






