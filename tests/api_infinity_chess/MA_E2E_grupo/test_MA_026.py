import pytest
from src.utils.logger_config import logger 
from src.api_infinity_chess.generar_info_curso import  crear_grupo, obtener_grupo, eliminar_grupo , codigo_curso, obtener_lista_grupos, verificar_eliminacion

@pytest.mark.smoke
def test_E2E_grupo(get_url):
    logger.info("Iniciando test MA_026.")
    logger.info("Obteniendo codigo de una materia.")
    CODCURSO = codigo_curso(get_url)
    logger.info("Crear nuevo grupo.")
    codigo_grupo=crear_grupo(get_url,CODCURSO)
    logger.info("Obtener grupo creado.")
    codigo_grupo_obtenido= obtener_grupo(get_url,CODCURSO,codigo_grupo)
    logger.info("Eliminar grupo.")
    response = eliminar_grupo(get_url,codigo_grupo_obtenido["CODGRUPO"])
    logger.debug(f"Este es el response: {response.json()}")
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.debug(f"Nombre grupo eliminado {codigo_grupo_obtenido["NOMBREGRUPO"]}")
    assert response.status_code==200
    lista_grupos = obtener_lista_grupos(get_url,CODCURSO)
    verificar_eliminacion(lista_grupos,codigo_grupo)
    logger.info("Test completado.")