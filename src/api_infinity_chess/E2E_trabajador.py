import requests
from src.utils.logger_config import logger
from src.utils.payload.payload_crear_trabajador import crear_payload_valido, crear_payload_para_actualizar
from src.api_infinity_chess.obtener_trabajadores import obtener_datos_de_trabajador
from src.utils.response_500 import response_500

def crear_trabajador_E2E(get_url):
        payload = crear_payload_valido()
        logger.debug(f"Payload: {payload}.")
        response = enviar_POST_E2E (get_url, payload)
        response_500(response)
        logger.info(f"Codigo de respuesta: {response.status_code}.")
        logger.info("Trabajador creado correctamente.")
        return response.json().get("CODTRABAJADOR")

def enviar_POST_E2E (get_url, payload):     #
        endpoint = "agregarTrabajador"
        url_final = get_url + endpoint
        logger.info(f"Enviando POST a {url_final}")
        return requests.post(url_final, json=payload)

def obtener_trabajador_E2E(get_url, codigo_trabajador):
        response = enviar_GET_E2E (get_url, codigo_trabajador)
        logger.info(f"Código de respuesta: {response.status_code}.")
        logger.debug(f"Response: {response.json()}.")
        info = obtener_datos_de_trabajador(response, logger)
        assert info["CODTRABAJADOR"]
        return response.json()

def enviar_GET_E2E (get_url, codigo_trabajador):
        endpoint = "obtenerTrabajador/" + codigo_trabajador
        url_final = get_url + endpoint
        logger.info(f"Enviando GET a {url_final}.")
        return requests.get(url_final)

def actualizar_trabajador_E2E (get_url, trabajador):
        logger.info("Editar datos del trabajador creado.")
        payload = crear_payload_para_actualizar(trabajador)
        logger.info(f"Payload: {payload}.")
        response = enviar_PUT_E2E(get_url, payload, trabajador.get("CODTRABAJADOR"))
        logger.info(f"Estatus code {response.status_code}.")
        logger.debug(f"Response: {response.json()}.")
        return response.json()

def enviar_PUT_E2E (get_url, payload, codigo_trabajador):     #
        endpoint = "actualizarDatosTrabajador/"
        url_final = get_url + endpoint + codigo_trabajador
        logger.info(f"Enviando PUT a {url_final}")
        response = requests.put(url_final, json=payload)
        response_500(response)
        return response

def eliminar_trabajador_E2E (get_url, codigo_trabajador):
        enviar_DELETE_E2E (get_url, codigo_trabajador)

def enviar_DELETE_E2E (get_url, CODTRABAJADOR):
        endpoint = "eliminarTrabajador/" + CODTRABAJADOR
        url_delete = get_url + endpoint
        logger.info(f"Enviando DELETE a {url_delete}")
        response = requests.delete(url_delete)
        return response