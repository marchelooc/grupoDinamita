import requests
import pytest
import random
from src.api_infinityChess.obtenerTutores import obtenerTutoresInactivos

@pytest.mark.smoke
def test_cambioDeEstadoDeTutorActivo (getUrl):
     listaTutores = obtenerTutoresInactivos(getUrl)
     CODTUTOR = random.choice(listaTutores)["CODTUTOR"]
     print(f"Modificando estado del tutor: {CODTUTOR}")
     endpoint = "actualizarEstadoTutor/" + CODTUTOR
     payload = {
          "ESTADO" : "Activo"
     }
     urlFinal = getUrl + endpoint
     response = requests.put(urlFinal, json=payload)
     assert response.status_code == 200