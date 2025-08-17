import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_nombre_similar1, payload_materia_nombre_similar2
from src.api_infinity_chess.materia import crear_materia, eliminar_materia, verificar_curso_nombre, cantidad_de_materias_mismo_nombre

@pytest.mark.functional
def test_validar_comportamiento_obetener_materias_con_nombres_repetidos(get_url):
    logger.info("Iniciando test MOCM024.")
    crear_materia(get_url, payload_materia_nombre_similar1)
    crear_materia(get_url, payload_materia_nombre_similar2)
    response = verificar_curso_nombre("FilosofiaREP", get_url)
    logger.debug(f"ESTE ES EL RESPONSE {response}.")
    assert response.status_code == 200
    logger.debug(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response")
    assert_validar_response_schema(response,cargar_schema("schema_lista_materias.json")) 
    cantidad_de_materias_mismo_nombre(response, "FilosofiaREP")
    eliminar_materia(get_url, "REPE1")
    eliminar_materia(get_url, "REPE2")
    logger.info("Test MOCM024 realizado.")
