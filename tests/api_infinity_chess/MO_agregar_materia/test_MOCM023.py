import requests
import pytest
from src.utils.response_500 import response_500
from src.assertions.add import assert_validar_schema_input, assert_validar_response_schema
from src.utils.generador_codigo import generar_nom_materia, generar_cod
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_correcta, headers_json
from src.api_infinity_chess.materia import crear_materia, eliminar_materia_con_header

@pytest.mark.smoke
def test_agregar_una_materia_sin_headers_de_tipo_json(get_url):
    logger.info("Iniciando test MOCM023.")
    logger.info("Iniciando test MOCM022.")
    logger.debug("El curso a crear es: Taller")
    logger.debug(f"este es el payload generado:{payload_materia_correcta}")
    logger.info("Validando schema del input.")
    assert_validar_schema_input(payload_materia_correcta,cargar_schema("schema_materias.json"))
    response = crear_materia(get_url, payload_materia_correcta)
    response_500(response)
    assert response.status_code == 201
    eliminar_materia_con_header(get_url, "2025Taller", headers_json)
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_materias.json"))
    logger.info("Test MOCM023 realizado.")