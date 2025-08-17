import requests
from src.utils.logger_config import logger
from src.utils.payload.payload_tutor import (
    crear_payload_tutor,crear_payload_update_tutor, 
    crear_payload_update_tutor_apellido, 
    crear_payload_update_tutor_nombre, 
    crear_payload_update_tutor_celular, 
    crear_payload_update_nombre_apellido, 
    crear_payload_update_nombre_vacio, 
    crear_payload_update_apellido_vacio, 
    crear_payload_update_numero_vacio, 
    crear_payload_update_nombre_caracteres,
    crear_payload_update_apellido_caracteres,
    crear_payload_update_celular_menor_caracteres,
    crear_payload_update_celular_mayor_caracteres,
    crear_payload_update_celular__caracteres_no_numericos,
    crear_payload_update_apellido_caracteres_especiales,
    crear_payload_update_nombre_caracteres_especiales,
    crear_payload_update_celular_repetido,
    crear_payload_update_body_vacio,
    crear_payload_update_nombre_40_caracteres,
    crear_payload_update_apellido_40_caracteres,
    crear_payload_update_espacios,
    crear_payload_update_guion_apostrofes,
    crear_payload_update_cod_pais
    )

from src.utils.response_500 import response_500
from src.utils.response_500 import response_500

def crear_tutor(get_url):
    logger.info(f"Generando Payload.")
    payload = crear_payload_tutor()
    logger.debug(f"Payload: {payload}.")
    tutor = enviar_solicitud_post(get_url,payload)
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json().get("CODTUTOR") 

def obtener_tutor(get_url, cod_tutor):
    logger.info(f"Obteniendo tutor creado.")
    tutor = enviar_solicitud_get(get_url,cod_tutor)
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor(get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_tutor (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_nombre (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_tutor_nombre (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_apellido (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_tutor_apellido (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_celular (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_tutor_celular (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_nombre_apellido (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_nombre_apellido (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_nombre_vacio (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_nombre_vacio (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_apellido_vacio (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_apellido_vacio (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_numero_vacio (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_numero_vacio (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_nombre_caracteres (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_nombre_caracteres (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_apellido_caracteres (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_apellido_caracteres (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_celular_menor_caracteres (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_celular_menor_caracteres (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_celular_mayor_caracteres (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_celular_mayor_caracteres (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_celular_caracteres_no_numericos (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_celular__caracteres_no_numericos (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_caracteres_especiales_apellido (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_apellido_caracteres_especiales (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_caracteres_especiales_nombre (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_nombre_caracteres_especiales (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_numero_cel_repetido (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_celular_repetido (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_body_vacio (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_body_vacio (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_nombre_40_caracteres (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_nombre_40_caracteres (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_apellido_40_caracteres (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_apellido_40_caracteres (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_espacios (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_espacios (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_guion_apostrofes (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_guion_apostrofes (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def actualizar_tutor_cod_pais (get_url,tutor):
    logger.info(f"Editando payload.")
    payload = crear_payload_update_cod_pais (tutor)
    logger.info(f"Payload: {payload}.")
    tutor = enviar_solicitud_put(get_url,payload,tutor.get("CODTUTOR"))
    logger.info(f"Estatus code {tutor.status_code}.")
    logger.debug(f"Response: {tutor.json()}.")
    return tutor.json()

def eliminar_tutor(get_url,cod_tutor):
    enviar_solicitud_delete(get_url,cod_tutor)
    logger.debug(f"Eliminado.")

def enviar_solicitud_post(get_url, payload, headers=None):
    endpoint = "agregarTutor"
    url_final = get_url + endpoint
    logger.info(f"Enviando POST a {url_final}.")
    response = requests.post(url_final, json=payload, headers=headers)
    response_500(response)
    return response

def enviar_solicitud_get(get_url, cod_tutor, headers=None):
    endpoint = "obtenerTutor/"
    url_final = get_url + endpoint + cod_tutor
    logger.info(f"Enviando GET a {url_final}.")
    response = requests.get(url_final, headers=headers)
    return response

def enviar_solicitud_put(get_url, payload, cod_tutor):
    endpoint = "actualizarTutor/"
    url_final = get_url + endpoint + cod_tutor
    logger.info(f"Enviando PUT a {url_final}.")
    response = requests.put(url_final, json=payload)
    response_500(response)
    return response

def enviar_solicitud_delete(get_url, cod_tutor, headers=None):
    endpoint = "eliminarTutor/"
    url_final = get_url + endpoint + cod_tutor
    logger.info(f"Enviando DELETE a {url_final}.")
    response = requests.delete(url_final, headers=headers)
    return response