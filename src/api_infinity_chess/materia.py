from src.api_infinity_chess.obtener_curso import obtener_cursos
import requests
import random
from src.utils.payload.payloads_materias import payload_materia_repetida
from src.utils.logger_config import logger

def existe_materia_repetida(nombre_materia_buscada) -> bool:
    listaMaterias = obtener_cursos("https://backend.clubinfinitychess.com/")
    return any(m["CURSO"] == nombre_materia_buscada for m in listaMaterias)

def crear_materia_repetida(get_Url, endpoint):
    urlFinal = get_Url + endpoint
    response_crear = requests.post(urlFinal, json=payload_materia_repetida)
    assert response_crear.status_code == 201

def obtener_nombre_materia_aleatoria(get_url):
    endpoint = "obtenerCursos/Modulo 4"
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    listaCursos = response.json()
    return random.choice(listaCursos)["CURSO"]
    
def verificar_curso_nombre(curso, get_url):
    endpoint = "verificarCurso/" + curso
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET {lista_url}.")
    return requests.get(lista_url)

def verificar_curso_nombre_con_header(curso, get_url, tipo_header):
    endpoint = "verificarCurso/" + curso
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET {lista_url}.")
    return requests.get(lista_url, headers=tipo_header)

def crear_materia(get_url, pyload_de_materia):
    endpoint = "agregarCurso"
    urlFinal = get_url + endpoint
    response_crear = requests.post(urlFinal, json = pyload_de_materia)
#    assert response_crear.status_code == 201
    logger.info(f"Código de respuesta del post: {response_crear.status_code}.")
    return response_crear

def eliminar_materia(get_url, cod_materia):
    endpoint = "eliminarCurso/" + cod_materia
    urlFinal = get_url + endpoint
    response_eliminar = requests.delete(urlFinal)
#    assert response_eliminar.status_code == 200
    logger.info(f"Código de respuesta del delete: {response_eliminar.status_code}.")
    return response_eliminar

def eliminar_materia_con_header(get_url, cod_materia, tipo_header):
    endpoint = "eliminarCurso/" + cod_materia
    urlFinal = get_url + endpoint
    response_eliminar = requests.delete(urlFinal, headers=tipo_header)
#    assert response_eliminar.status_code == 200
    logger.info(f"Código de respuesta del delete: {response_eliminar.status_code}.")
    return response_eliminar

def cantidad_de_materias_mismo_nombre(response, nombre_materia):
    respuestaJSON = response.json()
    cursos_filtrados = [item for item in respuestaJSON if item.get("CURSO") == nombre_materia]
    logger.info(f"La cantidad de cursos con nombre repetido de FilosofiaREP es de: {len(cursos_filtrados)}.")
    assert len(cursos_filtrados) >= 2

def recuperar_cursos_sede(get_url, nombre_sede):
    endpoint = "obtenerCursos/" + nombre_sede
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET {lista_url}.")
    return requests.get(lista_url)
