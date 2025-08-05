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



def obtener_nombre_grupo_existente(get_url, CODCURSO,lista_cursos):
    cursos_verificados = set()

    while True:
        endpoint = f"obtenerGrupo/{CODCURSO}/Modulo 4"
        response = requests.get(get_url + endpoint)
        response.raise_for_status()
        grupos = response.json()

        if grupos:
            return random.choice(grupos)["NOMBREGRUPO"]

        cursos_verificados.add(CODCURSO)

        cursos_restantes = [curso["CODCURSO"] for curso in lista_cursos if curso["CODCURSO"] not in cursos_verificados]

        if not cursos_restantes:

            raise ValueError("No se encontraron grupos creados en ningún curso.")

        CODCURSO = random.choice(cursos_restantes)
