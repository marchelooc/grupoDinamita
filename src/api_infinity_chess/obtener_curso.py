import requests
import random
def obtener_cursos(get_url):
    endpoint = "obtenerCursos/Modulo 4"
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    listaCursos = response.json()
    return listaCursos


