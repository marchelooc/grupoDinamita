import requests
import pytest
from src.assertions.add import assert_validar_schema_input , assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.generador_codigo import generar_codigo

@pytest.mark.smoke
def test_verificar_actualizacion_tutor_inexistente (get_url):
     CODTUTOR = generar_codigo()
     #print(f"Modificando estado del tutor: {CODTUTOR}")
     endpoint = "actualizarEstadoTutor/" + CODTUTOR
     payload = {
          "ESTADO" : "Activo"
     }
     assert_validar_schema_input(payload, cargar_schema("schema_estado.json"))
     url_final = get_url + endpoint
     response = requests.put(url_final, json=payload)
     assert response.status_code == 404
