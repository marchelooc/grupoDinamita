import requests
from src.utils.logger_config import logger

def enviar_DELETE(get_url, CODTRABAJADOR):
    endpoint = "eliminarTrabajador/" + CODTRABAJADOR
    url_delete = get_url + endpoint
    logger.info(f"Enviando DELETE a {url_delete}")
    return requests.delete(url_delete)

def enviar_DELETE_sin_CODTRABAJADOR(get_url):
    endpoint = "eliminarTrabajador/"
    lista_url = get_url + endpoint
    logger.info(f"Enviando DELETE a {lista_url}.")
    return requests.delete(lista_url)

def enviar_POST_para_DELETE(get_url, CODTRABAJADOR):
    endpoint = f"obtenerTrabajador/{CODTRABAJADOR}"
    url = get_url + endpoint
    logger.info(f"Enviando POST a {url}")
    return requests.post(url)

def enviar_DELETE_con_URL_inexistente(get_url, CODTRABAJADOR):
    endpoint = "eliminarTrabajadorees/" + CODTRABAJADOR #Endpoint mal escrito intencionalente
    lista_url = get_url + endpoint
    logger.info(f"Enviando DELETE a {lista_url}.")
    return requests.delete(lista_url)

