import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_a_eliminar

@pytest.mark.smoke
def test_validar_comportamiento_al_eliminar_materia_con_grupos(get_url):
    logger.info("Iniciando test MOCM032.")
    logger.info("creando curso para eliminar: Mecatronica con cod 2025MECA")
    url_final = get_url + "agregarCurso"
    requests.post(url_final, json=payload_materia_a_eliminar)
    logger.info("creando grupos para el curso")
    url_final = get_url + "agregarGrupo/2025MECA/Modulo 4"
#    requests.post(url_final, json=payload_materia_a_eliminar)

    logger.debug("eliminando Mecatronica con cod 2025MECA")
    url_final = get_url + "eliminarCurso/2025MECA"
    logger.info(f"Enviando DELETE {url_final}.")
    response = requests.delete(url_final)
    assert response.status_code == 200
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_eliminar_materia.json"))
    logger.info("Test MOCM032 realizado.")
