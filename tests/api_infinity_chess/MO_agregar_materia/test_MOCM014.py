import pytest
from src.assertions.add import assert_validar_schema_input, assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_nombre_largo
from src.api_infinity_chess.materia import crear_materia, eliminar_materia

@pytest.mark.negative
@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue MOCBUG01: HTTP incorrecto", run=True)
def test_validar_elLimite_maximo_de_caracteres_del_campo_CURSO(get_url):
    logger.info("Iniciando test MOCM0014.")
    logger.debug("El curso a crear es: Taller")
    logger.debug(f"este es el payload generado:{payload_materia_nombre_largo}")
    logger.info("Validando schema del input.")
    assert_validar_schema_input(payload_materia_nombre_largo,cargar_schema("schema_materias.json"))
    response = crear_materia(get_url, payload_materia_nombre_largo)
    eliminar_materia(get_url, "2025CAPORALES")
    logger.debug(f"ESTE ES EL RESPONSE {response}.")
    assert response.status_code == 400
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.debug("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_materias.json"))
    logger.info("Test MOCM014 realizado.")
    