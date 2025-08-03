import requests
import pytest
import random
from src.api_infinity_chess.obtener_tutores import obtener_tutores_inactivos
from src.assertions.add import assert_validar_schema_input , assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema

@pytest.mark.smoke
def test_cambio_de_estado_de_tutor_activo (get_url):
     lista_tutores = obtener_tutores_inactivos(get_url)
     CODTUTOR = random.choice(lista_tutores)["CODTUTOR"]
     endpoint = "actualizarEstadoTutor/" + CODTUTOR
     payload = {
          "ESTADO" : "Activo"
     }
     assert_validar_schema_input(payload, cargar_schema("schema_estado.json"))
     url_final = get_url + endpoint
     response = requests.put(url_final, json=payload)
     assert response.status_code == 200
     assert_validar_response_schema(response,cargar_schema("schema_tutor.json"))