import requests
import random
import json
from src.utils.generador_codigo import generar_codigo
from src.utils.logger_config import logger
from typing import Dict, Any, Literal, Iterable, Optional

def obtener_trabajadores(get_url):      #SVT001,
    endpoint = "obtenerTrabajadores/NACIONAL"
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    lista_trabajadores = response.json()
    return lista_trabajadores

def obtener_trabajador_aleatorio (get_url):     #SVT001,
    lista_trab = obtener_trabajadores(get_url)
    return random.choice(lista_trab)["CODTRABAJADOR"]

def obtener_nombre_trabajador_aleatorio (get_url):
    lista_trab = obtener_trabajadores(get_url)
    return random.choice(lista_trab)["NOMBRETRABAJADOR"]

def obtener_nombre_de_trabajador(get_url):
    logger.info("Obtener nombre de trabajador existente aleatorio.")
    NOMBRETRABAJADOR = obtener_nombre_trabajador_aleatorio (get_url)
    logger.debug(f"Trabajador elegido: {NOMBRETRABAJADOR}.")
    return NOMBRETRABAJADOR

def obtener_codigo_de_trabajador(get_url):
    logger.info("Obtener un trabajador existente aleatorio.")
    CODTRABAJADOR = obtener_trabajador_aleatorio (get_url)
    logger.debug(f"Trabajador elegido: {CODTRABAJADOR}.")
    return CODTRABAJADOR

def obtener_codigo_de_trabajador_inexistente():
    logger.info("Generar codigo inexistente.")
    CODTRABAJADOR = generar_codigo()
    logger.debug(f"El codigo inexistente es: {CODTRABAJADOR}.")
    return CODTRABAJADOR

def obtener_codigo_de_trabajador_invalido():
    logger.info("Usar un codigo de trabajador invalido.")
    CODTRABAJADOR = "203$%%00105XYZ@@"
    logger.debug(f"El codigo invalido es: {CODTRABAJADOR}.")
    return CODTRABAJADOR

def enviar_GET(get_url, CODTRABAJADOR):     #SVT001, SVT002, SVT005, SVT018, SVT019
    endpoint = "obtenerTrabajador/" + CODTRABAJADOR
    url_final = get_url + endpoint
    logger.info(f"Enviando GET a {url_final}.")
    return requests.get(url_final)

def enviar_POST_para_GET(get_url, CODTRABAJADOR):       #SVT020
    endpoint = f"obtenerTrabajador/{CODTRABAJADOR}"
    url = get_url + endpoint
    logger.info(f"Enviando POST a {url}(endpoint diseñado para GET)")
    return requests.post(url)

def enviar_GET_sin_CODTRABAJADOR(get_url):      #SVT003,
    endpoint = "obtenerTrabajador/"
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET a {lista_url}.")
    return requests.get(lista_url)

def enviar_GET_con_URL_inexistente(get_url, CODTRABAJADOR):     #SVT004
    endpoint = "obtenerTrabajadorees/" + CODTRABAJADOR #Endpoint mal escrito intencionalente
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET a {lista_url}.")
    return requests.get(lista_url)

def obtener_datos_de_trabajador(response, logger) -> Dict[str, Any]:        #SVT001,
    try:
        data = response.json()
    except json.JSONDecodeError:
        raise AssertionError(f"Respuesta no es JSON válido. Body: {response.text[:300]!r}")
    if isinstance(data, list):
        assert data, "La lista no puede estar vacía"
        trabajador = data[0]
    elif isinstance(data, dict):
        trabajador = data
    else:
        raise AssertionError(f"Formato inesperado de respuesta: {type(data)}")
    nombre = trabajador.get("NOMBRETRABAJADOR")
    codigo = trabajador.get("CODTRABAJADOR")
    fecha_nac = trabajador.get("FECHANACIMIENTOTRABAJADOR")
    rol = trabajador.get("ROLTRABAJADOR")
    logger.info("Detalles del trabajador recuperado:")
    logger.info(f"Nombre: {nombre}")
    logger.info(f"Codigo: {codigo}")
    logger.info(f"Fecha de nacimiento: {fecha_nac}")
    logger.info(f"Rol: {rol}")
    return {
        "NOMBRETRABAJADOR": nombre,
        "CODTRABAJADOR": codigo,
        "FECHANACIMIENTOTRABAJADOR": fecha_nac,
        "ROLTRABAJADOR": rol,
        "RAW": trabajador,
    }

def obtener_contraseña_trabajador(response: Literal['https://backend.clubinfinitychess.com/']):     #SVT005
    try:
        data = response.json()
    except json.JSONDecodeError:
        raise AssertionError(f"Respuesta no es JSON válido. Body: {response.text[:300]!r}")
    if isinstance(data, list):
        assert data, "La lista no puede estar vacía"
        trabajador = data[0]
    elif isinstance(data, dict):
        trabajador = data
    else:
        raise AssertionError(f"Formato inesperado de respuesta: {type(data)}")
    codigo = trabajador.get("CODTRABAJADOR")
    contra = trabajador.get("CONTRASEÑA")
    logger.info("Detalles del trabajador recuperado:")
    logger.info(f"Codigo: {codigo}")
    logger.info(f"Contraseña: {contra}")
    return {
        "CODTRABAJADOR": codigo,
        "CONTRASEÑA": contra,
        "RAW": trabajador,
    }

def verificar_estructura(response, logger, campos_requeridos: Optional[Iterable[str]] = None) -> Dict[str, Any]:        #SVT018
    if campos_requeridos is None:
        campos_requeridos = [
            "CODTRABAJADOR",
            "NOMBRETRABAJADOR",
            "FECHANACIMIENTOTRABAJADOR",
            "ROLTRABAJADOR",
            "HUELLATRABAJADOR",
            "CONTRASEÑA",
            "ESTADO",
        ]
    try:
        data = response.json()
    except json.JSONDecodeError:
        raise AssertionError(f"Respuesta no es JSON válido. Body: {response.text[:300]!r}")
    if isinstance(data, list):
        assert data, "La lista no puede estar vacía"
        trabajador = data[0]
    elif isinstance(data, dict):
        trabajador = data
    else:
        raise AssertionError(f"Formato inesperado de respuesta: {type(data)}")
    for campo in campos_requeridos:
        logger.debug(f"Existe el campo: {campo}")
        assert campo in trabajador, f"Falta el campo obligatorio '{campo}' en la respuesta"
    return trabajador

def obtener_trabajador_por_Id(get_url, codigo):
    endpoint = "obtenerTrabajador/" + codigo
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    lista_trabajadores = response.json()
    return lista_trabajadores