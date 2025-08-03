
import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema

@pytest.mark.smoke
def test_validar_estructura_de_respuesta(get_url):
    endpoint = "obtenerTutoresActivos"
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 200
    assert_validar_response_schema(response,cargar_schema("schema_lista_tutores.json"))
    lista_tutores = response.json()
    estructura_tutor = {"CODTUTOR","NOMBRETUTOR","APELLIDOTUTOR","FECHANACIMIENTOTUTOR","CELULARTUTOR","GENEROTUTOR", "OCUPACION", "CORREO", "ESTADO","CELULARALTERNATIVO"}
    for tutor in lista_tutores:
        campos_tutor = set(tutor.keys())
        campos_faltan = estructura_tutor - campos_tutor
        assert not campos_faltan , f"CamposFaltantes: {campos_faltan} del tutor {tutor}"