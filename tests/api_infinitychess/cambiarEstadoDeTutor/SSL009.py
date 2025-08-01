import requests
import pytest
import random
from src.api_infinityChess.obtenerTutores import obtenerTutoresActivos
from utils.generadorCodigo import generarCodigo

@pytest.mark.smoke
def test_verificarActualizacionTutorInexistente (getUrl):
     CODTUTOR = generarCodigo()
     print(f"Modificando estado del tutor: {CODTUTOR}")
     endpoint = "actualizarEstadoTutor/" + CODTUTOR
     payload = {
          "ESTADO" : "Activo"
     }
     urlFinal = getUrl + endpoint
     response = requests.put(urlFinal, json=payload)
     assert response.status_code == 404