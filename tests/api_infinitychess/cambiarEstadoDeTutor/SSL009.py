import requests
import pytest
import random
from src.obtenerTutores import obtenerTutoresActivos
from src.generadorCodigo import generarCodigo

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