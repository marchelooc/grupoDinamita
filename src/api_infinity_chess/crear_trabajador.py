import requests
import json
from src.utils.payload.payload_crear_trabajador import crear_payload_valido
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.response_500 import response_500
from src.utils.logger_config import logger

def enviar_POST(get_url, payload):     #
    endpoint = "agregarTrabajador"
    url_final = get_url + endpoint
    logger.info(f"Enviando POST a {url_final}")
    response = requests.post(url_final, json=payload)
    response_500(response)
    return response

def enviar_POST_sin_body(get_url):     #
    endpoint = "agregarTrabajador"
    url_final = get_url + endpoint
    logger.info(f"Enviando POST a {url_final}")
    response = requests.post(url_final)
    response_500(response)
    return response

def tierdown_enviar_DELETE(get_url, CODTRABAJADOR):     #
    endpoint = "eliminarTrabajador/" + CODTRABAJADOR
    url_delete = get_url + endpoint
    logger.info(f"Enviando DELETE a {url_delete}")
    response = requests.delete(url_delete)
    response_500(response)
    return response

def enviar_POST_textplain(get_url, payload, headers=None):
    headers = {"Content-Type": "text/plain"} # Se envia el mismo payload con Content-Type: text/plain
    body = json.dumps(payload)
    endpoint = "agregarTrabajador"
    url_final = get_url + endpoint
    logger.info(f"Enviando POST a {url_final} con Content Type text plain")
    logger.debug(f"Body (text plain): {body}")
    logger.debug(payload)
    response = requests.post(url_final, data=body, headers=headers)
    response_500(response)
    return response

def mostrar_trabajador(payload):
    logger.info("Mostrar los datos del trabajador creado.")
    CODTRABAJADOR = payload.get("CODTRABAJADOR")
    logger.debug(f"El codigo del trabajador creado es: {CODTRABAJADOR}.")
    NOMBRETRABAJADOR = payload.get("NOMBRETRABAJADOR")
    logger.debug(f"El codigo del trabajador creado es: {NOMBRETRABAJADOR}.")
    FECHANACIMIENTOTRABAJADOR = payload.get("FECHANACIMIENTOTRABAJADOR")
    logger.debug(f"El codigo del trabajador creado es: {FECHANACIMIENTOTRABAJADOR}.")
    ROLTRABAJADOR = payload.get("ROLTRABAJADOR")
    logger.debug(f"El codigo del trabajador creado es: {ROLTRABAJADOR}.")
    CODSEDE = payload.get("CODSEDE")
    logger.debug(f"El codigo del trabajador creado es: {CODSEDE}.")

def crear_un_trabajador (get_url,payload):
    logger.info("Obtener datos de un trabajador para registrarlo en el sistema.")
    response = enviar_POST (get_url, payload)
    response_500(response)
    logger.info("Validando schema de entrada del payload.")
    assert_validar_schema_input(payload, cargar_schema("schema_trabajador.json"))
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 201
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_trabajador.json"))
    logger.info("Trabajador creado correctamente.")
    return response.json()