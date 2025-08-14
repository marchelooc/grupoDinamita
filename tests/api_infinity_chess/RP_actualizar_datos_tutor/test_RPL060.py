import pytest
from src.utils.logger_config import logger 
from src.api_infinity_chess.E2E_tutor import  crear_tutor, obtener_tutor, actualizar_tutor_cod_pais, eliminar_tutor

@pytest.mark.smoke
def test_RPL060_actualizar_numero_cel_con_codigo_pais (get_url):
    logger.info("Iniciando test RPL060.")
    logger.info("Crear nuevo tutor.")
    cod_tutor = crear_tutor(get_url)
    logger.info("Obtener tutor creado.")
    tutor = obtener_tutor(get_url, cod_tutor)
    logger.info("Editar el numero de celular añadiendo el codigo de pais.")
    tutor_actualizado = actualizar_tutor_cod_pais(get_url,tutor[0])
    logger.info("Eliminar tutor.")
    eliminar_tutor(get_url,tutor_actualizado.get("CODTUTOR"))
    logger.info("Obtener tutor creado.")
    tutor = obtener_tutor(get_url, cod_tutor)
    logger.info("Test completado.")