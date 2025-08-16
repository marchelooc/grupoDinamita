import pytest
from src.api_infinity_chess.generar_info_curso import realizar_eliminacion, validar_respuesta
from src.utils.generador_codigo import generar_cod_letras
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue MABUG001: EL endpoint no responde correctamente cuando se elimina un grupo con id invalido con sol letras", run=True)
def test_verificar_que_se_elimine_un_grupo_con_id_solo_letras(get_url):
    logger.info("Iniciando test MAM027.")
    codigo=generar_cod_letras()
    logger.debug(f"codigo generado: {codigo}")
    logger.debug(f"Eliminando grupo con codigo: {codigo}")
    response = realizar_eliminacion(get_url,codigo)
    logger.debug(f"response:{response.json()}")
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code==404
    validar_respuesta(response)
    logger.info("Test completado.") 