import requests
from src.utils.logger_config import logger

def enviar_solicitud_sede (get_url, Sede):
    logger.info(get_url)
    endpoint = f"obtenerTutores/{Sede}"
    lista_url = get_url + endpoint
    logger.debug (lista_url)
    response = requests.get(lista_url)
    return response