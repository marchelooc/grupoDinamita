import pytest
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_correcta
from src.api_infinity_chess.materia import crear_materia, eliminar_materia, verificar_curso_nombre, recuperar_cursos_sede, validar_curso_dentro_de_cursos_sede_response

@pytest.mark.smoke
@pytest.mark.functional
def test_validar_flujo_de_eliminación(get_url):
    logger.info("Iniciando test MOCM008.")
    logger.info("Creando el curso")
    crear_materia(get_url, payload_materia_correcta)
    logger.info("Obteniendo el curso recien creado")
    verificar_curso_nombre("Taller", get_url)
    logger.info("Eliminando el curso recien creado")
    eliminar_materia(get_url, "2025Taller")
    logger.info("recuperando la lista de cursos de la sede Modulo 4")
    response = recuperar_cursos_sede(get_url, "Modulo 4")
    logger.debug(f"ESTE ES EL RESPONSE {response}.")
    logger.info("verificando que el curso Taller no exista en la sede Modulo 4")
    validar_curso_dentro_de_cursos_sede_response(response, "2025Taller")
    logger.info("Test MOCM008 realizado.")