import requests
import pytest

@pytest.mark.smoke
def test_sinTutoresActivos(getUrl):
     endpoint = "obtenerTutoresActivos"
     lista_url = getUrl + endpoint
     response = requests.get(lista_url)
     assert response.status_code == 200
     listaTutores = response.json()
     if len(listaTutores) == 0:
          assert True
     else :
          for tutor in listaTutores:
               assert tutor.get("ESTADO") == "Activo", f"Tutor inactivo encontrado: {tutor}"
