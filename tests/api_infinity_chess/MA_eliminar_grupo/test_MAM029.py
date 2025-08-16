import pytest
from src.api_infinity_chess.generar_info_curso import realizar_eliminacion, validar_respuesta
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue MABUG001: EL endpoint no responde correctamente cuando se elimina un grupo con id con caracteres mayores a 30", run=True)
def test_validar_comortamiento_de_eliminar_con_id_largo(get_url):
    logger.info("Iniciando test MAM029.")
    codigo="2025grupomayorde30caracteresenId"
    logger.debug(f"codigo generado: {codigo}")
    logger.debug(f"Eliminando grupo con codigo: {codigo}")
    response = realizar_eliminacion(get_url,codigo)
    logger.debug(f"response:{response.json()}")
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code==400
    validar_respuesta(response)
    logger.info("Test completado.")