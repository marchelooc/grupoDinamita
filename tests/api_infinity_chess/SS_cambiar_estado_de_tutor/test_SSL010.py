import requests
import pytest
import random
from src.api_infinity_chess.obtener_tutores import obtener_tutores_activos
from src.assertions.add import assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue SSBUG001: Aceptar valor de estado invalido",run=True)
def test_validación_de_valor_inválido_en_campo_estado (get_url):
     logger.info("Iniciando test SSL010.")
     logger.info("Obtener un tutor aleatorio.")
     lista_tutores = obtener_tutores_activos(get_url)
     CODTUTOR = random.choice(lista_tutores)["CODTUTOR"]
     logger.debug(f"Tutor seleccionado: {CODTUTOR}.")
     endpoint = "actualizarEstadoTutor/" + CODTUTOR
     payload = {
          "ESTADO" : "Pendiente"
     }
     logger.debug(f"Payload: {payload}")
     logger.info("Validando schema del payload.")
     assert_validar_schema_input(payload, cargar_schema("schema_estado.json"))
     url_final = get_url + endpoint
     logger.info(f"Enviando PUT a {url_final}.")
     response = requests.put(url_final, json=payload)
     logger.info(f"Código de respuesta: {response.status_code}.")
     assert response.status_code == 400
     logger.debug(f"Response: {response.json()}")
     logger.info("Test completado.")
