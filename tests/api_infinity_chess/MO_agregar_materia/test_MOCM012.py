import pytest
from src.assertions.add import assert_validar_schema_input,assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.api_infinity_chess.materia import crear_materia, eliminar_materia, existe_materia_repetida
from src.utils.payload.payloads_materias import generar_materia_aleatoria
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue MOCBUG01: HTTP incorrecto", run=True)
def test_validar_comportamiento_al_agregar_curso_con_CODCURSO_duplicado(get_url):
    logger.info("Iniciando test MOCM012.")
    payload = generar_materia_aleatoria()
    logger.info(f"El curso a crear es: {payload['CURSO']}")
    logger.debug(f"este es el payload generado:{payload}")
    logger.info("Validando schema del input.")
    assert_validar_schema_input(payload,cargar_schema("schema_materias.json"))
    logger.info("Creando Curso repetido si es que no existe.")
    if not existe_materia_repetida(payload['CURSO'] ):
            logger.info("Creando materia repetida.")    
            crear_materia(get_url, payload)
    logger.info("Intentando crear nuevamente el curso.")
    response = crear_materia(get_url, payload)
    logger.debug(f"ESTE ES EL RESPONSE {response}.")
    eliminar_materia(get_url, payload["CODCURSO"])
    assert response.status_code == 409
    logger.debug(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_materias.json"))
    logger.info("Test MOCM012 realizado.")
    
