import requests
import pytest
import random
from src.api_infinity_chess.obtener_tutores import obtener_tutores_activos
from src.assertions.add import assert_validar_schema_input , assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema

@pytest.mark.smoke
def test_solicitud_con_headers_Content_Type_application_x_www_form_urlencoded (get_url):
     lista_tutores = obtener_tutores_activos(get_url)
     CODTUTOR = random.choice(lista_tutores)["CODTUTOR"]
     #print(f"Modificando estado del tutor: {CODTUTOR}")
     endpoint = "actualizarEstadoTutor/" + CODTUTOR
     payload = {
          "ESTADO" : "Activo"
     }
     headers = {
          "Accept": "application/json",
          "Content-Type": "application/x-www-form-urlencoded"
     }
     assert_validar_schema_input(payload, cargar_schema("schema_estado.json"))
     url_final = get_url + endpoint
     response = requests.put(url_final, headers=headers, json=payload)
     assert response.status_code == 200 
     assert_validar_response_schema(response,cargar_schema("schema_tutor.json"))