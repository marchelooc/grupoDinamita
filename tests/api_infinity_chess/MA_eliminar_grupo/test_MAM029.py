import pytest
from src.api_infinity_chess.generar_info_curso import realizar_eliminacion
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
def test_validar_comortamiento_de_eliminar_con_id_largo(get_url):
    logger.info("Iniciando test MAM029.")
    codigo="2025grupomayorde30caracteresenId" #id de grupo largo
    logger.debug(f"codigo generado: {codigo}")
    #eliminar grupo
    response = realizar_eliminacion(get_url,codigo)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code==400
    try:
        data = response.json()
    except ValueError:
        data = None 
    if data:
        logger.info("Validando schema del response.")
        assert_validar_response_schema(response,cargar_schema("schema_eliminar_grupo.json"))
    logger.info("Test completado.")