import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema

@pytest.mark.smoke
def test_solicitud_con_headers(get_url):
    endpoint = "obtenerTutoresActivos"
    lista_url = get_url + endpoint
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.get(lista_url, headers=headers)
    assert response.status_code == 200
    assert_validar_response_schema(response,cargar_schema("schema_lista_tutores.json"))
    lista_tutores = response.json()
    for tutor in lista_tutores:
        assert tutor.get("ESTADO") == "Activo", f"Tutor inactivo encontrado: {tutor}"
