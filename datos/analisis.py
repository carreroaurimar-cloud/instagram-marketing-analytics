import csv

# Abrir los datos de Instagram
with open("datos/instagram_data.csv", "r") as archivo:
    datos = list(csv.DictReader(archivo))

# Calcular las interacciones de cada publicación
for post in datos:
    post["interacciones"] = (
        int(post["likes"])
        + int(post["comments"])
        + int(post["shares"])
        + int(post["saves"])
    )

# Encontrar la publicación con más interacciones
mejor_post = max(datos, key=lambda post: post["interacciones"])

print("La publicación con mejor rendimiento fue:")
print("Post:", mejor_post["post"])
print("Interacciones:", mejor_post["interacciones"])
