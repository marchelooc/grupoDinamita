import pytest
from src.utils.logger_config import logger 
from src.api_infinity_chess.generar_info_curso import  crear_grupo, obtener_grupo, eliminar_grupo , codigo_curso

@pytest.mark.smoke
def test_E2E_grupo(get_url):
    logger.info("Iniciando test MA_026.")
    logger.info("Obteniendo codigo de una materia.")
    CODCURSO = codigo_curso(get_url)
    logger.info("Crear nuevo grupo.")
    codigo_grupo=crear_grupo(get_url,CODCURSO)
    logger.info("Obtener grupo creado.")
    obtener_grupo(get_url,CODCURSO,codigo_grupo)
    logger.info("Eliminar grupo.")
    response = eliminar_grupo(get_url,codigo_grupo)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code==200
    logger.info("Test completado.")