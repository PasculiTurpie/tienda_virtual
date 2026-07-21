import requests

respuesta = requests.get("https://www.programacionfacil.org/", timeout=5)

respuesta2 = requests.get("https://www.gtd.cl/", timeout=5)

contenido = respuesta.content.decode('utf-8')

print(respuesta)
print(respuesta2)
print(contenido)