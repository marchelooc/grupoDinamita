import requests
import pytest
import random
from src.api_infinity_chess.obtener_tutores import obtener_tutores_activos
from src.assertions.add import assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema

@pytest.mark.smoke
def test_validación_de_valor_inválido_en_campo_estado (get_url):
     lista_tutores = obtener_tutores_activos(get_url)
     CODTUTOR = random.choice(lista_tutores)["CODTUTOR"]
     #print(f"Modificando estado del tutor: {CODTUTOR}")
     endpoint = "actualizarEstadoTutor/" + CODTUTOR
     payload = {
          "ESTADO" : "Pendiente"
     }
     assert_validar_schema_input(payload, cargar_schema("schema_estado.json"))
     url_final = get_url + endpoint
     response = requests.put(url_final, json=payload)
     assert response.status_code == 400