import requests
from src.utils.logger_config import logger 

def enviar_solicitud (get_url, CODTUTOR):
    logger.info(get_url)
    endpoint = f"obtenerEstudiantesTutor/{CODTUTOR}"
    lista_url = get_url + endpoint
    logger.debug(lista_url)
    response = requests.get(lista_url)
    return response

def validar_lista_un_estudiante (lista_tutores):
    assert len (lista_tutores) > 0
    assert len (lista_tutores) < 2