import pytest
from src.api_infinity_chess.obtener_trabajadores import obtener_trabajador_aleatorio, enviar_GET, obtener_datos_de_trabajador
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_obtener_trabajador_existente_por_Id_valido(get_url):
    logger.info("Inicio de test SVT001.")
    logger.info("Obtener un trabajador existente aleatorio.")
    CODTRABAJADOR = obtener_trabajador_aleatorio (get_url)
    logger.debug(f"Trabajador elegido: {CODTRABAJADOR}.")
    response = enviar_GET (get_url, CODTRABAJADOR)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 200
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_obtener_trabajador.json"))
    info = obtener_datos_de_trabajador(response, logger)
    assert info["CODTRABAJADOR"]
    logger.info("Test completado.")