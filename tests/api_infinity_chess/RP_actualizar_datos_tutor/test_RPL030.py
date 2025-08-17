import pytest
from src.utils.logger_config import logger 
from src.api_infinity_chess.E2E_tutor import  crear_tutor, obtener_tutor, actualizar_tutor_apellido_vacio, eliminar_tutor

@pytest.mark.functional
@pytest.mark.negative
def test_RPL030_actualizar_tutor_con_campo_apellido_vacio(get_url):
    logger.info("Iniciando test RPL030.")
    logger.info("Crear nuevo tutor.")
    cod_tutor = crear_tutor(get_url)
    logger.info("Obtener tutor creado.")
    tutor = obtener_tutor(get_url, cod_tutor)
    logger.info("Editar apellido vacio del tutor.")
    tutor_actualizado = actualizar_tutor_apellido_vacio(get_url,tutor[0])
    logger.info("Eliminar tutor.")
    eliminar_tutor(get_url,tutor_actualizado.get("CODTUTOR"))
    logger.info("Obtener tutor creado.")
    tutor = obtener_tutor(get_url, cod_tutor)
    logger.info("Test completado.")