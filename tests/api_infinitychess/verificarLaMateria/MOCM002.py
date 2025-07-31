import requests
import pytest
import random
from src.obtenerMateria import obtenerMateria

@pytest.mark.smoke
def test_ValidarQueSeRecuperenLaMateriaConNombreDeCurso(getUrl):
    listaMaterias = obtenerMateria(getUrl)
    CURSO = random.choice(listaMaterias)["CURSO"]
    print(f"Materia escogida es: {CURSO}")
    endpoint = "verificarCurso/" + CURSO
    lista_url = getUrl + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 200

