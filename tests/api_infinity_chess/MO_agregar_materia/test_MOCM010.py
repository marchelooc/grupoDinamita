import requests
import pytest
from src.utils.response_500 import response_500
from src.assertions.add import assert_validar_schema_input, assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_sin_CODCURSO
from src.api_infinity_chess.materia import crear_materia, eliminar_materia

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue MOCBUG01: HTTP incorrecto", run=True)
def test_validar_comportamiento_al_agregar_curso_sin_CODCURSO(get_url):
    logger.info("Iniciando test MOCM010.")
    logger.debug("El curso a crear es: Taller")
    logger.debug(f"este es el payload generado:{payload_materia_sin_CODCURSO}")
    logger.info("Validando schema del input.")
    assert_validar_schema_input(payload_materia_sin_CODCURSO,cargar_schema("schema_materias.json"))
    response = crear_materia(get_url, payload_materia_sin_CODCURSO)
    response_500(response)
    assert response.status_code == 422
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_materias.json"))
    logger.info("Test MOCM010 realizado.")
    