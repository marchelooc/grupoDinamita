import pytest
from src.api_infinity_chess.generar_info_curso import codigo_curso, realizar_eliminacion, crear_grupo , obtener_lista_grupos, validar_respuesta, verificar_eliminacion
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_verificar_que_se_elimine_un_grupo_con_id_valido(get_url):
    logger.info("Iniciando test MAM019.")
    CODMATERIA = codigo_curso(get_url)
    logger.debug(f"Codigo materia seleccionado: {CODMATERIA}.")
    logger.info("Creando grupo")
    codigo=crear_grupo(get_url,CODMATERIA)
    logger.info("Eliminando grupo")
    response = realizar_eliminacion(get_url,codigo)
    logger.debug(f"response:{response.json()}")
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code==200
    lista_grupos = obtener_lista_grupos(get_url,CODMATERIA)
    verificar_eliminacion(lista_grupos,codigo)
    validar_respuesta(response)
    logger.info("Test completado.") 