import requests
import random
from src.api_infinity_chess.obtener_tutores import obtener_tutores_activos
from src.utils.logger_config import logger 

def obtenerTutorAleatorio (get_url):
     lista_tutores = obtener_tutores_activos(get_url)
     return random.choice(lista_tutores)["CODTUTOR"]

def enviarSolicitud(get_url, CODTUTOR, payload, headers=None):
     endpoint = "actualizarEstadoTutor/" + CODTUTOR
     url_final = get_url + endpoint
     logger.info(f"Enviando PUT a {url_final}.")
     return requests.put(url_final, json=payload, headers=headers)
