import requests
import pytest
import random
from src.obtenerTutores import obtenerTutoresActivos

@pytest.mark.smoke
def test_validaciónDeValorInválidoEnCampoEstado (getUrl):
     listaTutores = obtenerTutoresActivos(getUrl)
     CODTUTOR = random.choice(listaTutores)["CODTUTOR"]
     print(f"Modificando estado del tutor: {CODTUTOR}")
     endpoint = "actualizarEstadoTutor/" + CODTUTOR
     payload = {
          "ESTADO" : ""
     }
     urlFinal = getUrl + endpoint
     response = requests.put(urlFinal, json=payload)
     assert response.status_code == 400