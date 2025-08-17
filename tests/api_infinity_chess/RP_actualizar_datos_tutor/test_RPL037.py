import pytest
from src.utils.logger_config import logger 
from src.api_infinity_chess.E2E_tutor import  crear_tutor, obtener_tutor, actualizar_tutor_celular_menor_caracteres, eliminar_tutor

@pytest.mark.functional
@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue RPBUG011: Actualiza los datos del tutor cuando el numero de cel es menor a 8 digitos",run=True)
def test_RPL037_actualizar_tutor_con_celular_menor_8_digitos (get_url):
    logger.info("Iniciando test RPL037.")
    logger.info("Crear nuevo tutor.")
    cod_tutor = crear_tutor(get_url)
    logger.info("Obtener tutor creado.")
    tutor = obtener_tutor(get_url, cod_tutor)
    logger.info("Editar numero de celular de tutor con menos de 8 caracteres.")
    tutor_actualizado = actualizar_tutor_celular_menor_caracteres(get_url,tutor[0])
    logger.info("Eliminar tutor.")
    eliminar_tutor(get_url,tutor_actualizado.get("CODTUTOR"))
    logger.info("Obtener tutor creado.")
    tutor = obtener_tutor(get_url, cod_tutor)
    logger.info("Test completado.")