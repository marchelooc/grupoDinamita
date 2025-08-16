import requests
from src.utils.logger_config import logger

def peticion_agregar_motivo (get_url, payload):
    logger.info(get_url)    
    endpoint = "agregarMotivo" 
    lista_url = get_url + endpoint
    response = requests.post(lista_url, json=payload)
    return response