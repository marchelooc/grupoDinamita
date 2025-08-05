import requests
import pytest
from src.assertions.add import assert_validar_schema_input , assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.generador_codigo import generar_codigo
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_verificar_actualizacion_tutor_inexistente (get_url):
     logger.info("Iniciando test SSL009.")
     logger.info("Generar un tutor inexistente.")
     CODTUTOR = generar_codigo()
     logger.debug(f"Tutor seleccionado: {CODTUTOR}.")
     endpoint = "actualizarEstadoTutor/" + CODTUTOR
     payload = {
          "ESTADO" : "Activo"
     }
     logger.debug(f"Payload: {payload}")
     logger.info("Validando schema del payload.")
     assert_validar_schema_input(payload, cargar_schema("schema_estado.json"))
     url_final = get_url + endpoint
     logger.info(f"Enviando PUT a {url_final}.")
     response = requests.put(url_final, json=payload)
     logger.info(f"Código de respuesta: {response.status_code}.")
     assert response.status_code == 404
     logger.info("Test completado.")
