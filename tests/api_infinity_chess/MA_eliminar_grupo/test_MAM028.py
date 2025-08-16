import pytest
from src.api_infinity_chess.generar_info_curso import realizar_eliminacion, validar_respuesta
from src.utils.generador_codigo import generar_cod_caracteres
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue MABUG001: EL endpoint no responde correctamente cuando se elimina un grupo con id solo con caracteres especiales", run=True)
def test_verificar_que_se_elimine_un_grupo_con_id_caracteres_especiales(get_url):
    logger.info("Iniciando test MAM028.")
    codigo=generar_cod_caracteres()
    logger.debug(f"codigo generado: {codigo}")
    logger.debug(f"Eliminando grupo con codigo: {codigo}")
    response = realizar_eliminacion(get_url,codigo)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code==400
    validar_respuesta(response)
    logger.info("Test completado.")