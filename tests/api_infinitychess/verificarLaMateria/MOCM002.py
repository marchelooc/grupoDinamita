import requests
import pytest
import random
from src.obtenerCurso import obtenerCursos

@pytest.mark.smoke
def test_ValidarQueSeRecuperenLaMateriaConNombreDeCurso(getUrl):
    listaMaterias = obtenerCursos(getUrl)
    CURSO = random.choice(listaMaterias)["CURSO"]
    print(f"Materia escogida es: {CURSO}")
    endpoint = "verificarCurso/" + CURSO
    lista_url = getUrl + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 200

