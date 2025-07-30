
import requests
import pytest

@pytest.mark.smoke
def test_ValidarEstructuraDeRespuesta(getUrl):
    endpoint = "obtenerTutoresActivos"
    lista_url = getUrl + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 200
    listaTutores = response.json()
    estructuraRequerida = {"CODTUTOR","NOMBRETUTOR","APELLIDOTUTOR","FECHANACIMIENTOTUTOR","CELULARTUTOR","GENEROTUTOR", "OCUPACION", "CORREO", "ESTADO","CELULARALTERNATIVO"}
    for tutor in listaTutores:
        camposTutor = set(tutor.keys())
        camposFaltan = estructuraRequerida - camposTutor
        assert not camposFaltan , f"CamposFaltantes: {camposFaltan} del tutor {tutor}"
