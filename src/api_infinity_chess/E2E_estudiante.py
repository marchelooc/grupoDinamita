import requests
from src.utils.logger_config import logger
from src.utils.payload.payload_estudiante import crear_payload_estudiante,crear_payload_update_estudiante
from src.utils.response_500 import response_500

def crear_estudiante(get_url):
     logger.info(f"Generando Payload.")
     payload = crear_payload_estudiante()
     logger.debug(f"Payload: {payload}.")
     estudiante = enviar_solicitud_post(get_url,payload)
     logger.info(f"Estatus code {estudiante.status_code}.")
     logger.debug(f"Response: {estudiante.json()}.")
     return estudiante.json().get("CODESTUDIANTE") 
     
def obtener_estudiante(get_url, cod_estudiante):
     logger.info(f"Obteniendo estudiante creado.")
     estudiante = enviar_solicitud_get(get_url,cod_estudiante)
     logger.info(f"Estatus code {estudiante.status_code}.")
     logger.debug(f"Response: {estudiante.json()}.")
     return estudiante.json()

def actualizar_estudiante(get_url,estudiante):
     logger.info(f"Editando payload.")
     payload = crear_payload_update_estudiante (estudiante)
     logger.info(f"Payload: {payload}.")
     estudiante = enviar_solicitud_put(get_url,payload,estudiante.get("CODESTUDIANTE"))
     logger.info(f"Estatus code {estudiante.status_code}.")
     logger.debug(f"Response: {estudiante.json()}.")
     return estudiante.json()

def eliminar_estudiante(get_url,cod_estudiante):
     enviar_solicitud_delete(get_url,cod_estudiante)
     logger.debug(f"Eliminado.")

def enviar_solicitud_post(get_url, payload, headers=None):
     endpoint = "agregarEstudiante"
     url_final = get_url + endpoint
     logger.info(f"Enviando POST a {url_final}.")
     response = requests.post(url_final, json=payload, headers=headers)
     response_500(response)
     return response

def enviar_solicitud_get(get_url, cod_estudiante, headers=None):
     endpoint = "obtenerEstudiante/"
     url_final = get_url + endpoint + cod_estudiante
     logger.info(f"Enviando GET a {url_final}.")
     response = requests.get(url_final, headers=headers)
     return response

def enviar_solicitud_put(get_url, payload, cod_estudiante):
     endpoint = "actualizarEstudiante/"
     url_final = get_url + endpoint + cod_estudiante
     logger.info(f"Enviando PUT a {url_final}.")
     response = requests.put(url_final, json=payload)
     response_500(response)
     return response

def enviar_solicitud_delete(get_url, cod_estudiante, headers=None):
     endpoint = "eliminarEstudiante/"
     url_final = get_url + endpoint + cod_estudiante
     logger.info(f"Enviando DELETE a {url_final}.")
     response = requests.delete(url_final, headers=headers)
     return response