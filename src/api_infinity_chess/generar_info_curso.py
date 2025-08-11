import random
import requests
from src.api_infinity_chess.obtener_curso import obtener_cursos
from src.utils.payload.generar_payload_grupo import cargar_payload_grupo
from src.utils.generador_codigo import generar_cod, obtener_dias
from src.utils.logger_config import logger

def codigo_curso(get_url):
    lista_cursos = obtener_cursos(get_url)
    CODCURSO = random.choice(lista_cursos)["CODCURSO"]
    return CODCURSO

def realizar_peticion(get_url,payload):
    end_point = "agregarGrupo"
    url_final = get_url + end_point
    logger.info(f"Enviando POST a {url_final}.")
    return requests.post(url_final, json=payload)

def crear_grupo(get_url,CODCURSO):
    end_point = "agregarGrupo"
    nombre_grupo="grupo doble"
    dias=obtener_dias()
    codigo= generar_cod(nombre_grupo)
    payload=cargar_payload_grupo(CODCURSO,nombre_grupo,dias,"21:00",0,30,codigo)
    url_final = get_url + end_point
    requests.post(url_final, json=payload)

def solicitar_peticion(get_url,CODMATERIA,headers):
    end_point = "obtenerGrupo/"+CODMATERIA+"/Modulo 4"
    lista_url = get_url + end_point
    logger.info(f"Enviando GET a {lista_url}.")
    return requests.get(lista_url, headers=headers)