import pytest
from src.utils.logger_config import logger 
from src.api_infinity_chess.E2E_tutor import  crear_tutor, obtener_tutor, actualizar_tutor_caracteres_especiales_apellido, eliminar_tutor

@pytest.mark.functional
@pytest.mark.negative
#@pytest.mark.xfail(reason="Knwon issue RPBUG013: Actualiza los datos de un tutor cuando el apellido contiene caracteres especiales",run=True)
def test_RPL041_actualizar_tutor_con_caracteres_especiales_apellido (get_url):
    logger.info("Iniciando test RPL041.")
    logger.info("Crear nuevo tutor.")
    cod_tutor = crear_tutor(get_url)
    logger.info("Obtener tutor creado.")
    tutor = obtener_tutor(get_url, cod_tutor)
    logger.info("Editar el apellido de tutor con caracteres especiales.")
    tutor_actualizado = actualizar_tutor_caracteres_especiales_apellido(get_url,tutor[0])
    logger.info("Eliminar tutor.")
    eliminar_tutor(get_url,tutor_actualizado.get("CODTUTOR"))
    logger.info("Obtener tutor creado.")
    tutor = obtener_tutor(get_url, cod_tutor)
    logger.info("Test completado.")