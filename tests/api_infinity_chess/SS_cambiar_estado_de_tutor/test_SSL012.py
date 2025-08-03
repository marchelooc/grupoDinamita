import requests
import pytest
import random
from src.api_infinity_chess.obtener_tutores import obtener_tutores_activos
from src.assertions.add import assert_validar_schema_input 
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_solicitud_sin_body (get_url):
     logger.info("Iniciando test SSL012.")
     lista_tutores = obtener_tutores_activos(get_url)
     CODTUTOR = random.choice(lista_tutores)["CODTUTOR"]
     logger.debug(f"Tutor seleccionado: {CODTUTOR}.")
     endpoint = "actualizarEstadoTutor/" + CODTUTOR
     url_final = get_url + endpoint
     payload = {
     }
     logger.info("Validando schema del payload.")
     assert_validar_schema_input(payload, cargar_schema("schema_estado.json"))
     logger.info(f"Enviando PUT a {url_final}.")
     response = requests.put(url_final)
     logger.info(f"Código de respuesta: {response.status_code}.")
     assert response.status_code == 400
     logger.info("Test completado.")
