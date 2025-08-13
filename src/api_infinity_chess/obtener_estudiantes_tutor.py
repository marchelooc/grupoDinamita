import requests
from src.utils.logger_config import logger 

def enviar_solicitud (get_url, CODTUTOR):
    logger.info(get_url)
    endpoint = f"obtenerEstudiantesTutor/{CODTUTOR}"
    lista_url = get_url + endpoint
    logger.debug(lista_url)
    response = requests.get(lista_url)
    return response