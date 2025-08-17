import pytest
from src.api_infinity_chess.generar_info_curso import codigo_curso, realizar_eliminacion, crear_grupo , validar_respuesta, eliminar_grupo, obtener_lista_grupos,verificar_eliminacion
from src.utils.logger_config import logger

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue MABUG008: El endpoint no responde correctamente cuando se elimina un grupo con id que ya no existe", run=True)
def test_verificar_que_se_elimine_un_grupo_por_segunda_vez(get_url):
    logger.info("Iniciando test MAM022.")
    CODMATERIA = codigo_curso(get_url)
    logger.debug(f"Codigo materia seleccionado: {CODMATERIA}.")
    logger.info("Creando grupo")
    codigo=crear_grupo(get_url,CODMATERIA)
    logger.debug(f"Eliminando grupo con codigo: {codigo}")
    eliminar_grupo(get_url,codigo)
    lista_grupos = obtener_lista_grupos(get_url,CODMATERIA)
    verificar_eliminacion(lista_grupos,codigo)
    logger.debug(f"Eliminando grupo nuevamente con el codigo: {codigo}")
    response = realizar_eliminacion(get_url,codigo)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code==404
    validar_respuesta(response)
    logger.info("Test completado.") 