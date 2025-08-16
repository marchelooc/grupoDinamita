import requests
from src.utils.logger_config import logger 

def obtener_tutores_sede (get_url):
    endpoint = "obtenerTutores/Modulo 4"
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET a {lista_url}")
    response = requests.get(lista_url)
    return response

def obtener_tutores_sede_sin_tutores_asignados (get_url):
    endpoint = "obtenerTutores/Modulo 5"
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET a {lista_url}")
    response = requests.get(lista_url)
    return response

def obtener_tutores_sede_invalida (get_url):
    endpoint = "obtenerTutores/ASDFJASDKNXCV"
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET a {lista_url}")
    response = requests.get(lista_url)
    return response

def obtener_tutores__sede_escrita_MAYUSCULAS_minusculas (get_url):
    endpoint = "obtenerTutores/MoDuLo 4"
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET a {lista_url}")
    response = requests.get(lista_url)
    return response

def obtener_tutores_sede_con_formato_invalido (get_url):
    endpoint = "obtenerTutores/$%&/(&%$)"
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET a {lista_url}")
    response = requests.get(lista_url)
    return response