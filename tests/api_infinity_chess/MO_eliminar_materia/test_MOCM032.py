import pytest
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_a_eliminar
from src.api_infinity_chess.materia import crear_materia, eliminar_materia

@pytest.mark.smoke
def test_validar_comportamiento_al_eliminar_materia_con_grupos(get_url):
    logger.info("Iniciando test MOCM032.")
    crear_materia(get_url, payload_materia_a_eliminar)


    logger.info("creando grupos para el curso")
    url_final = get_url + "agregarGrupo/2025MECA/Modulo 4"
#    requests.post(url_final, json=payload_materia_a_eliminar)

    logger.debug("eliminando Mecatronica con cod 2025MECA")
    response = eliminar_materia(get_url, "2025MECA")
    assert response.status_code == 200
    logger.info("Test MOCM032 realizado.")
