import pytest
from src.api_infinity_chess.generar_info_curso import codigo_curso, crear_grupo_limite, obtener_lista_grupos_con_limite, eliminar_grupo, verificar_limite_lleno, obtener_lista_grupos, verificar_eliminacion
from src.utils.logger_config import logger

@pytest.mark.functional
def test_verificar_comportamiento_del_limite_lleno(get_url):
    logger.info("Iniciando test MAM023.")
    CODMATERIA = codigo_curso(get_url)
    logger.debug(f"Curso seleccionado: {CODMATERIA}")
    limite_diponible=4 
    logger.info("creando grupo limite disponible")
    codigo=crear_grupo_limite(get_url,CODMATERIA,limite_diponible)
    lista_grupos = obtener_lista_grupos_con_limite(get_url,CODMATERIA)
    verificar_limite_lleno(lista_grupos,codigo)
    logger.debug(f"Eliminando grupo con codigo: {codigo}")
    response=eliminar_grupo(get_url,codigo)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 200
    lista_grupos = obtener_lista_grupos(get_url,CODMATERIA)
    verificar_eliminacion(lista_grupos,codigo)
    logger.info("Test completado.")