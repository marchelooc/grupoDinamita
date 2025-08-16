import requests
from src.utils.logger_config import logger
from src.utils.payload.payload_crear_trabajador import crear_payload_valido
from src.api_infinity_chess.crear_trabajador import enviar_POST
from src.utils.response_500 import response_500

def crear_trabajador(get_url):
        logger.info(f"Generando Payload.")
        payload = crear_payload_valido()
        logger.debug(f"Payload: {payload}.")
        trabajador = enviar_POST(get_url,payload)
        logger.info(f"Estatus code {trabajador.status_code}.")
        logger.debug(f"Response: {trabajador.json()}.")
        logger.info("Trabajador creado.")
        return trabajador.json().get("CODTRABAJADOR") 

def enviar_PUT (get_url, payload, trabajador):
        endpoint = "actualizarDatosTrabajador/"
        url_final = get_url + endpoint + trabajador
        logger.info(f"Enviando PUT a {url_final}")
        response = requests.put(url_final, json=payload)
        response_500(response)
        return response

def enviar_PUT_sin_payload (get_url, trabajador):
        endpoint = "actualizarDatosTrabajador/"
        url_final = get_url + endpoint + trabajador
        logger.info(f"Enviando PUT a {url_final}")
        response = requests.put(url_final)
        response_500(response)
        return response

def enviar_PUT_con_headers (get_url, payload, trabajador):
        headers = {
                "Accept": "application/json",
                "Content-Type": "text/plain",
                }
        endpoint = "actualizarDatosTrabajador/"
        url_final = get_url + endpoint + trabajador
        logger.info(f"Enviando PUT a {url_final}")
        response = requests.put(url_final, json=payload, headers=headers)
        response_500(response)
        return response

def enviar_PUT_con_endpoint_mal_escrito (get_url, payload, trabajador):
        endpoint = "actualizarDatosTrabajadoreess/"
        url_final = get_url + endpoint + trabajador
        logger.info(f"Enviando PUT a {url_final}")
        response = requests.put(url_final, json=payload)
        response_500(response)
        return response

def enviar_POST_por_PUT (get_url, payload):
        endpoint = "actualizarDatosTrabajador/"
        url_final = get_url + endpoint
        logger.info(f"Enviando POST a {url_final}")
        response = requests.post(url_final, json=payload)
        response_500(response)
        return response

def crear_trabajador_comp(get_url):
        logger.info(f"Generando Payload.")
        payload = crear_payload_valido()
        logger.debug(f"Payload: {payload}.")
        trabajador = enviar_POST(get_url,payload)
        logger.info(f"Estatus code {trabajador.status_code}.")
        logger.debug(f"Response: {trabajador.json()}.")
        logger.info("Trabajador creado.")
        return trabajador.json()