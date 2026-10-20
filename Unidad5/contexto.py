# Forma antigua
f = open("datos.txt", "r")
contenido = f.read()

# Forma moderna (Recomendada)
with open("datos.txt", "r") as f:
    contenido = f.read()
    f.name()
#¡Ya está cerrado automáticamente aqui!