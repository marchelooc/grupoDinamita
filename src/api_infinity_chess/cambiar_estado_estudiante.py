import requests
import random
from src.api_infinity_chess.obtener_estudiantes import obtener_estudiantes
from src.utils.logger_config import logger 

def obtener_estudiante_aleatorio (get_url):
     lista_estudiante = obtener_estudiantes(get_url)
     return random.choice(lista_estudiante)["CODESTUDIANTE"]

def enviar_solicitud(get_url, CODESTUDIANTE, payload, headers=None):
     endpoint = "actualizarEstadoEstudiante/" + CODESTUDIANTE
     url_final = get_url + endpoint
     logger.info(f"Enviando PUT a {url_final}.")
     return requests.put(url_final, json=payload, headers=headers)
