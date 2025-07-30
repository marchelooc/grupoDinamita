import requests
import pytest
import random
from src.obtenerTutores import obtenerTutoresActivos

@pytest.mark.smoke
def test_solicitudConHeaders_Content_Type_application_x_www_form_urlencoded (getUrl):
     listaTutores = obtenerTutoresActivos(getUrl)
     CODTUTOR = random.choice(listaTutores)["CODTUTOR"]
     print(f"Modificando estado del tutor: {CODTUTOR}")
     endpoint = "actualizarEstadoTutor/" + CODTUTOR
     payload = {
          "ESTADO" : "Activo"
     }
     headers = {
          "Accept": "application/json",
          "Content-Type": "application/x-www-form-urlencoded"
     }
     urlFinal = getUrl + endpoint
     response = requests.put(urlFinal, headers=headers, json=payload)
     assert response.status_code == 403 