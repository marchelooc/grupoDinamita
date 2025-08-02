import requests
import pytest

@pytest.mark.smoke
def test_VerificaciónDelCódigoDeRespuesta(getUrl):
    endpoint = "obtenerTutoresActivos"
    lista_url = getUrl + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 200