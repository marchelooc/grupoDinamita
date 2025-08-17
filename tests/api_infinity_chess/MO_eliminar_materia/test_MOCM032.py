import pytest
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import generar_materia_aleatoria
from src.api_infinity_chess.materia import crear_materia, eliminar_materia
from src.api_infinity_chess.generar_info_curso import crear_grupo
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue MOCBUG01: HTTP incorrecto", run=True)
def test_validar_comportamiento_al_eliminar_materia_con_grupos(get_url):
    logger.info("Iniciando test MOCM032.")
    payload = generar_materia_aleatoria()
    crear_materia(get_url, payload)
    logger.info(f"creando grupos para el curso: {payload['CURSO']}")
    crear_grupo(get_url, payload['CODCURSO'])
    logger.debug(f"eliminando {payload['CURSO']}")
    response = eliminar_materia(get_url, payload['CODCURSO'])
    logger.debug(f"ESTE ES EL RESPONSE {response}.")
    assert response.status_code == 400
    logger.info("Validando schema del response")
    assert_validar_response_schema(response,cargar_schema("schema_eliminar_materia.json")) 
    logger.info("Test MOCM032 realizado.")