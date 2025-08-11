import requests
import random
import json
from src.utils.logger_config import logger
from typing import Dict, Any, Literal, Iterable, Optional

def enviar_POST(get_url, payload):     #
    endpoint = "agregarTrabajador"
    url_final = get_url + endpoint
    logger.info(f"Enviando POST a {url_final}")
    return requests.post(url_final, json=payload)

def enviar_POST_sin_body(get_url):     #
    endpoint = "agregarTrabajador"
    url_final = get_url + endpoint
    logger.info(f"Enviando POST a {url_final}")
    return requests.post(url_final)

def tierdown_enviar_DELETE(get_url, CODTRABAJADOR):     #
    endpoint = "eliminarTrabajador/" + CODTRABAJADOR
    url_delete = get_url + endpoint
    logger.info(f"Enviando DELETE a {url_delete}")
    return requests.delete(url_delete)

def enviar_POST_textplain(get_url, payload, headers=None):
    headers = {"Content-Type": "text/plain"} # Se envia el mismo payload con Content-Type: text/plain
    body = json.dumps(payload)
    endpoint = "agregarTrabajador"
    url_final = get_url + endpoint
    logger.info(f"Enviando POST a {url_final} con Content Type text plain")
    logger.debug(f"Body (text plain): {body}")
    logger.debug(payload)
    return requests.post(url_final, data=body, headers=headers)