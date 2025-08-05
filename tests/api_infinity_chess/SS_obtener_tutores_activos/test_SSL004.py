import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_verificación_del_código_de_respuesta(get_url):
    logger.info("Iniciando test SSL004.")
    endpoint = "obtenerTutoresActivos"
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET a {lista_url}.")
    response = requests.get(lista_url)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 200
    lista_tutores = response.json()
    logger.debug(lista_tutores)
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_tutores.json"))
    logger.info("Test completado.")
