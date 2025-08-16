import pytest
from src.assertions.add import assert_validar_schema_input, assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_correcta
from src.api_infinity_chess.materia import crear_materia, eliminar_materia

@pytest.mark.smoke
@pytest.mark.functional
def test_agregar_una_materia_con_datos_válidos(get_url):
    logger.info("Iniciando test MOCM008.")
    logger.debug("El curso a crear es: Taller")
    logger.debug(f"este es el payload generado:{payload_materia_correcta}")
    logger.info("Validando schema del input.")
    assert_validar_schema_input(payload_materia_correcta,cargar_schema("schema_materias.json"))
    response = crear_materia(get_url, payload_materia_correcta)
    logger.debug(f"ESTE ES EL RESPONSE {response}.")
    assert response.status_code == 201
    eliminar_materia(get_url, "2025Taller")
    logger.debug(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_materias.json"))
    logger.info("Test MOCM008 realizado.")