import requests
import pytest
from src.utils.response_500 import response_500
from src.assertions.add import assert_validar_schema_input
from src.utils.generador_codigo import generar_nom_materia, generar_cod
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_sin_Nombre

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue MOCBUG02: Materia agregada sin nombre", run=True)
def test_validar_comportamiento_al_agregar_curso_sin_campo_CURSO(get_url):
    logger.info("Iniciando test MOCM011.")
    endpoint = "agregarCurso"
    logger.debug(f"este es el payload generado:{payload_materia_sin_Nombre}")
    logger.info("Validando schema del input.")
    assert_validar_schema_input(payload_materia_sin_Nombre,cargar_schema("schema_materias.json"))
    url_final = get_url + endpoint
    logger.info(f"Enviando POST {url_final}.")
    response = requests.post(url_final, json=payload_materia_sin_Nombre)
    assert response.status_code == 422
    logger.info(f"Código de respuesta: {response.status_code}.")
    url_final = get_url + "eliminarCurso/2025BIOLOGIA"
    logger.info(f"Enviando DELETE {url_final}.")
    requests.delete(url_final)
    logger.info("Test MOCM011 realizado.")
    