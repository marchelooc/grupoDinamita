import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_solicitud_sin_headers(get_url):
    logger.info("Iniciando test SSL006.")
    endpoint = "obtenerTutoresActivos"
    lista_url = get_url + endpoint
    headers = {
    }
    logger.info(f"Enviando GET a {lista_url}.")
    response = requests.get(lista_url, headers=headers)
    logger.debug(response.json)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 200
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_tutores.json"))
    lista_tutores = response.json()
    logger.debug(lista_tutores)
    logger.info("Validando lista tutores activos.")
    for tutor in lista_tutores:
        assert tutor.get("ESTADO") == "Activo", f"Tutor inactivo encontrado: {tutor}"
    logger.info("Validando lista tutores activos.")
