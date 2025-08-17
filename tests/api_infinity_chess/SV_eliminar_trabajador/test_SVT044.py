import pytest
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador
from src.api_infinity_chess.eliminar_trabajador import enviar_DELETE
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_eliminar_un_trabajador_existente_con_CODTRABAJADOR_valido (get_url):
    logger.info("Iniciando test SVT044.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)#precondicion
    response = enviar_DELETE (get_url, trabajador)
    logger.info(f"Codigo de respuesta DELETE: {response.status_code}")
    logger.debug(f"Response:{response.json()}.")
    assert response.status_code == 200
    assert_validar_response_schema(response,cargar_schema("schema_eliminar_trabajador.json"))
    logger.info("Test completado.")