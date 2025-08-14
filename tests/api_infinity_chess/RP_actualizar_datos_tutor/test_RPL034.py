import pytest
from src.utils.logger_config import logger 
from src.api_infinity_chess.E2E_tutor import  crear_tutor, obtener_tutor, actualizar_tutor_apellido_caracteres, eliminar_tutor

@pytest.mark.smoke
def test_RPL034_actualizar_tutor_con_campo_apellido_mayor_limite_permitido(get_url):
    logger.info("Iniciando test RPL034.")
    logger.info("Crear nuevo tutor.")
    cod_tutor = crear_tutor(get_url)
    logger.info("Obtener tutor creado.")
    tutor = obtener_tutor(get_url, cod_tutor)
    logger.info("Editar apellido del tutor con limite de caracteres mayor al permitido.")
    tutor_actualizado = actualizar_tutor_apellido_caracteres(get_url,tutor[0])
    logger.info("Eliminar tutor.")
    eliminar_tutor(get_url,tutor_actualizado.get("CODTUTOR"))
    logger.info("Obtener tutor creado.")
    tutor = obtener_tutor(get_url, cod_tutor)
    logger.info("Test completado.")