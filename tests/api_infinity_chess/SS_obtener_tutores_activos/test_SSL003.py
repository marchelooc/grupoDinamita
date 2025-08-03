import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema

@pytest.mark.smoke
def test_sin_tutores_activos(get_url):
     endpoint = "obtenerTutoresActivos"
     lista_url = get_url + endpoint
     response = requests.get(lista_url)
     assert response.status_code == 200
     assert_validar_response_schema(response,cargar_schema("schema_lista_tutores.json"))
     lista_tutores = response.json()
     if len(lista_tutores) == 0:
          assert True
     else :
          for tutor in lista_tutores:
               assert tutor.get("ESTADO") == "Activo", f"Tutor inactivo encontrado: {tutor}"
