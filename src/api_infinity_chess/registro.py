import requests
import random
from src.api_infinity_chess.obtener_estudiantes import obtener_estudiantes
from src.utils.logger_config import logger
from src.utils.response_500 import response_500 

def obtener_estudiante_aleatorio (get_url):
     lista_estudiante = obtener_estudiantes(get_url)
     return random.choice(lista_estudiante)["CODESTUDIANTE"]

def obtener_estudiante_aleatorio_completo (get_url):
     lista_estudiante = obtener_estudiantes(get_url)
     return random.choice(lista_estudiante)

def enviar_solicitud(get_url, payload, headers=None):
     endpoint = "agregarRegistro"
     url_final = get_url + endpoint
     logger.info(f"Enviando POST a {url_final}.")
     response = requests.post(url_final, json=payload, headers=headers)
     response_500(response)
     return response