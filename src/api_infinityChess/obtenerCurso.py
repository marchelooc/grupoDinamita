import requests
import random
def obtenerCursos(getUrl):
    endpoint = "obtenerCursos/Modulo 4"
    lista_url = getUrl + endpoint
    response = requests.get(lista_url)
    listaCursos = response.json()
    return listaCursos


def obtenerCodMateria(getUrl):
    cursos=obtenerCursos(getUrl)
    CODMATERIA = random.choice(cursos)["CODCURSO"]
    return CODMATERIA

def listaGrupos():
    
    return