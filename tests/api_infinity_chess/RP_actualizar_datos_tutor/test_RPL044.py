import pytest
from src.utils.logger_config import logger 
from src.api_infinity_chess.E2E_tutor import  crear_tutor, obtener_tutor, actualizar_tutor_numero_cel_repetido, eliminar_tutor

@pytest.mark.smoke
def test_RPL044_actualizar_tutor_con_numero_celular_repetido (get_url):
    logger.info("Iniciando test RPL044.")
    logger.info("Crear nuevo tutor.")
    cod_tutor = crear_tutor(get_url)
    logger.info("Obtener tutor creado.")
    tutor = obtener_tutor(get_url, cod_tutor)
    logger.info("Editar el numero de celular del tutor con numero repetido.")
    tutor_actualizado = actualizar_tutor_numero_cel_repetido(get_url,tutor[0])
    logger.info("Eliminar tutor.")
    eliminar_tutor(get_url,tutor_actualizado.get("CODTUTOR"))
    logger.info("Obtener tutor creado.")
    tutor = obtener_tutor(get_url, cod_tutor)
    logger.info("Test completado.")