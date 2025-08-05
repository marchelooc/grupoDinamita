import requests
import pytest

from src.assertions.add import assert_validar_schema_input
from src.utils.generador_codigo import generar_nom_materia
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue MOCBUG01: HTTP incorrecto", run=False)
def test_validar_comportamiento_al_agregar_curso_sin_CODCURSO(get_url):
    logger.info("Iniciando test MOCM010.")
    nombre_materia = generar_nom_materia()
    logger.debug(f"Curso aleatorio creado sin codcurso {nombre_materia}.")
    endpoint = "agregarCurso"
    payload = {
                "CODCURSO": "",
                "CURSO": nombre_materia, 
                "ESTADO": "activo",
                }
    logger.info("Validando schema del input.")
    assert_validar_schema_input(payload,cargar_schema("schema_materias.json"))
    url_final = get_url + endpoint
    logger.info(f"Enviando POST {url_final}.")
    response = requests.post(url_final, json=payload)
    assert response.status_code == 422
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Test MOCM010 realizado.")
    