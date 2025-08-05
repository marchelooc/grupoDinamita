import requests
import pytest

from src.assertions.add import assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger 

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue MOCBUG01: HTTP incorrecto", run=False)
def test_validar_comportamiento_al_agregar_un_curso_con_todos_los_campos_vacíos(get_url):
    logger.info("Iniciando test MOCM009.")
    endpoint = "agregarCurso"
    payload = {
                "CODCURSO": "",
                "CURSO": "",
                "ESTADO": "",
                }
    logger.debug("Curso aleatorio creado vacio.")
    logger.info("Validando schema del input.")
    assert_validar_schema_input(payload,cargar_schema("schema_materias.json"))
    url_final = get_url + endpoint
    logger.info(f"Enviando POST {url_final}.")
    response = requests.post(url_final, json=payload)
    assert response.status_code == 400
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Test MOCM008 realizado.")
    