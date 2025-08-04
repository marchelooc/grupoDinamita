from typing import Literal
import requests
import pytest
import random
from src.api_infinity_chess.obtener_trabajadores import obtener_trabajadores
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_validar_que_la_contraseña_se_muestre_cifrada(get_url: Literal['https://backend.clubinfinitychess.com/']):
    lista_trabajdores = obtener_trabajadores(get_url)
    CODTRABAJADOR = random.choice(lista_trabajdores)["CODTRABAJADOR"]
    logger.debug(f"Trabajador buscado: {CODTRABAJADOR}.")
    endpoint = "obtenerTrabajador/" + CODTRABAJADOR
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET a {lista_url}.")
    response = requests.get(lista_url)
    
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 200
    
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_obtener_trabajador.json")) #schema de salida
    
    logger.info("Obteniendo el JSON de la respuesta.")
    json_data = response.json()
    logger.debug(f"JSON recibido: {json_data!r}")
    trabajador = response.json()
    if isinstance(trabajador, list):
        assert trabajador, "La lista no puede estar vacía"
        trabajador = trabajador[0]
        
    logger.info("Test completado.")