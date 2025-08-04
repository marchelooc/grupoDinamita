import requests
import random
def obtener_cursos(get_url):
    endpoint = "obtenerCursos/Modulo 4"
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    listaCursos = response.json()
    return listaCursos


def obtener_cod_materia(get_url):
    cursos=obtener_cursos(get_url)
    CODMATERIA = random.choice(cursos)["CODCURSO"]
    return CODMATERIA



def obtener_nombre_grupo_existente(get_url, CODCURSO):
    endpoint = f"obtenerGrupo/{CODCURSO}/Modulo 4"
    response = requests.get(get_url + endpoint)
    response.raise_for_status()
    grupos = response.json()

    if not grupos:
        raise ValueError("No hay grupos existentes para duplicar.")

    nombre_grupo = random.choice(grupos)["NOMBREGRUPO"]
    return nombre_grupo