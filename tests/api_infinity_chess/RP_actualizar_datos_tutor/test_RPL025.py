import pytest
from src.utils.logger_config import logger 
from src.api_infinity_chess.E2E_tutor import  crear_tutor, obtener_tutor, actualizar_tutor_nombre_apellido, eliminar_tutor

@pytest.mark.functional
@pytest.mark.negative
def test_RPL025_actualizar_nombre_apellido_de_tutor_existente(get_url):
    logger.info("Iniciando test RPL025.")
    logger.info("Crear nuevo tutor.")
    cod_tutor = crear_tutor(get_url)
    logger.info("Obtener tutor creado.")
    tutor = obtener_tutor(get_url, cod_tutor)
    logger.info("Editar nombre y apellido del tutor.")
    tutor_actualizado = actualizar_tutor_nombre_apellido(get_url,tutor[0])
    logger.info("Eliminar tutor.")
    eliminar_tutor(get_url,tutor_actualizado.get("CODTUTOR"))
    logger.info("Obtener tutor creado.")
    tutor = obtener_tutor(get_url, cod_tutor)
    logger.info("Test completado.")