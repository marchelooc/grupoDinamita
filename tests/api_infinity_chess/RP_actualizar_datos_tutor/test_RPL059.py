import pytest
from src.utils.logger_config import logger 
from src.api_infinity_chess.E2E_tutor import  crear_tutor, obtener_tutor, actualizar_tutor_guion_apostrofes, eliminar_tutor

@pytest.mark.functional
def test_RPL059_actualizar_apellido_nombre_apellido_guion_apostrofes (get_url):
    logger.info("Iniciando test RPL059.")
    logger.info("Crear nuevo tutor.")
    cod_tutor = crear_tutor(get_url)
    logger.info("Obtener tutor creado.")
    tutor = obtener_tutor(get_url, cod_tutor)
    logger.info("Editar el nombre y apellido del tutor con guion y apostrofes.")
    tutor_actualizado = actualizar_tutor_guion_apostrofes(get_url,tutor[0])
    logger.info("Eliminar tutor.")
    eliminar_tutor(get_url,tutor_actualizado.get("CODTUTOR"))
    logger.info("Obtener tutor creado.")
    tutor = obtener_tutor(get_url, cod_tutor)
    logger.info("Test completado.")