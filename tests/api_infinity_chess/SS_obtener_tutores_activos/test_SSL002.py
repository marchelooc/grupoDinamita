
import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_validar_estructura_de_respuesta(get_url):
    logger.info("Iniciando test SSL002.")
    endpoint = "obtenerTutoresActivos"
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET a {lista_url}.")
    response = requests.get(lista_url)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 200
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_tutores.json"))
    lista_tutores = response.json()
    logger.info("Validando estructura de tutores activos.")
    estructura_tutor = {"CODTUTOR","NOMBRETUTOR","APELLIDOTUTOR","FECHANACIMIENTOTUTOR","CELULARTUTOR","GENEROTUTOR", "OCUPACION", "CORREO", "ESTADO","CELULARALTERNATIVO"}
    for tutor in lista_tutores:
        campos_tutor = set(tutor.keys())
        campos_faltan = estructura_tutor - campos_tutor
        assert not campos_faltan , f"CamposFaltantes: {campos_faltan} del tutor {tutor}"
    logger.info("Test completado.")
