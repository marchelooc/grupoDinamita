import requests
import pytest
import random
from src.api_infinity_chess.obtener_tutores import obtener_tutores_activos
from src.assertions.add import assert_validar_schema_input 
from src.utils.cargar_schema import cargar_schema

@pytest.mark.smoke
def test_solicitud_sin_body (get_url):
     lista_tutores = obtener_tutores_activos(get_url)
     CODTUTOR = random.choice(lista_tutores)["CODTUTOR"]
     #print(f"Modificando estado del tutor: {CODTUTOR}")
     endpoint = "actualizarEstadoTutor/" + CODTUTOR
     url_final = get_url + endpoint
     payload = {
     }
     assert_validar_schema_input(payload, cargar_schema("schema_estado.json"))
     response = requests.put(url_final)
     assert response.status_code == 400