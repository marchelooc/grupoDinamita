import pytest
from src.api_infinity_chess.generar_info_curso import realizar_eliminacion, validar_respuesta
from src.utils.generador_codigo import generar_codigo_caracteres_invalidos
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue MABUG001: El endpoint permite enviar un ID con formato y que contiene caracteres especiales", run=True)
def test_verificar_que_se_elimine_un_grupo_con_id_formato_caracteres_no_permitidos(get_url):
    logger.info("Iniciando test MAM020.")
    logger.info("Creando grupo")
    codigo=generar_codigo_caracteres_invalidos()
    logger.info("Eliminando grupo")
    response = realizar_eliminacion(get_url,codigo)
    logger.debug(f"response:{response.json()}")
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.debug(f"response:{response}")
    assert response.status_code==400
    validar_respuesta(response)
    logger.info("Test completado.") 