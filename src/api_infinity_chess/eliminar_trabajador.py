import requests
from src.utils.logger_config import logger

def enviar_DELETE(get_url, CODTRABAJADOR):
    endpoint = "eliminarTrabajador/" + CODTRABAJADOR
    url_delete = get_url + endpoint
    logger.info(f"Enviando DELETE a {url_delete}")
    return requests.delete(url_delete)

def enviar_DELETE_sin_CODTRABAJADOR(get_url):
    endpoint = "eliminarTrabajador/"
    lista_url = get_url + endpoint
    logger.info(f"Enviando DELETE a {lista_url}.")
    return requests.delete(lista_url)

def enviar_POST_para_DELETE(get_url, CODTRABAJADOR):
    endpoint = f"obtenerTrabajador/{CODTRABAJADOR}"
    url = get_url + endpoint
    logger.info(f"Enviando POST a {url}")
    return requests.post(url)

def enviar_DELETE_con_URL_inexistente(get_url, CODTRABAJADOR):
    endpoint = "eliminarTrabajadorees/" + CODTRABAJADOR #Endpoint mal escrito intencionalente
    lista_url = get_url + endpoint
    logger.info(f"Enviando DELETE a {lista_url}.")
    return requests.delete(lista_url)

def tierdown_eliminar_trabajador_creado(get_url, payload):
    logger.info("Obtener al trabajador creado.")
    CODTRABAJADOR = payload.get("CODTRABAJADOR")
    logger.debug(f"El codigo del trabajador creado es: {CODTRABAJADOR}.")
    response = tierdown_enviar_DELETE (get_url, CODTRABAJADOR)
    logger.info(f"Codigo de respuesta DELETE: {response.status_code}")
    assert response.status_code == 200

def tierdown_enviar_DELETE(get_url, CODTRABAJADOR):     #
    endpoint = "eliminarTrabajador/" + CODTRABAJADOR
    url_delete = get_url + endpoint
    logger.info(f"Enviando DELETE a {url_delete}")
    return requests.delete(url_delete)

def tierdown_eliminar_trabajador_editado(get_url, trabajador):
    logger.info("Obtener al trabajador creado.")
    response = tierdown_enviar_DELETE (get_url, trabajador)
    logger.info(f"Codigo de respuesta DELETE: {response.status_code}")
    assert response.status_code == 200

def tierdown_enviar_DELETE_edit(get_url, trabajador):
    endpoint = "eliminarTrabajador/" + trabajador
    url_delete = get_url + endpoint
    logger.info(f"Enviando DELETE a {url_delete}")
    return requests.delete(url_delete)