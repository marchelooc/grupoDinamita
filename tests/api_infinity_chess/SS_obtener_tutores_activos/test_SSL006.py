import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

<<<<<<< HEAD:tests/api_infinity_chess/MA_obtener_grupo/test_MAM010.py
@pytest.mark.negative
def test_obtener_grupos_de_una_materia_con_id_invalido_sede_modulo4(get_url):
    logger.info("Iniciando test MAM010.")
    #cursos=obtenerCursos(getUrl)
    CODMATERIA ="abcde"
    end_point = "obtenerGrupo/"+CODMATERIA+"/Modulo 4"
    logger.debug(f"Codigo materia seleccionado: {CODMATERIA}.")
    lista_url = get_url + end_point
    logger.info(f"Enviando GET a {lista_url}.")
=======
@pytest.mark.smoke
def test_solicitud_sin_headers(get_url):
    logger.info("Iniciando test SSL006.")
    endpoint = "obtenerTutoresActivos"
    lista_url = get_url + endpoint
>>>>>>> 818bf39e2e9685a9c75e5faa347ab9253cecefaa:tests/api_infinity_chess/SS_obtener_tutores_activos/test_SSL006.py
    headers = {
    }
    logger.info(f"Enviando GET a {lista_url}.")
    response = requests.get(lista_url, headers=headers)
    logger.debug(response.json)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 200
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_tutores.json"))
    lista_tutores = response.json()
    logger.debug(lista_tutores)
    logger.info("Validando lista tutores activos.")
    for tutor in lista_tutores:
        assert tutor.get("ESTADO") == "Activo", f"Tutor inactivo encontrado: {tutor}"
    logger.info("Validando lista tutores activos.")
