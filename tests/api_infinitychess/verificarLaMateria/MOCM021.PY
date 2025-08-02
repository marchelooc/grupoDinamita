import requests
import pytest
import random
from src.api_infinityChess.obtenerCurso import obtenerCursos
from src.assertions.add import assert_validarResponseSchema
from src.utils.cargarSchema import cargar_schema

#Validar comportamiento ante una materia con nombre de curso inexistente
@pytest.mark.exploratorio
def test_ValidarComportamientoAnteUnaMateriaConNombreDeCursoInexistente(getUrl):
    listaMaterias = obtenerCursos(getUrl)
    CURSO = random.choice(listaMaterias)["CURSO"]
    print(f"Materia escogida es: {CURSO}")
    endpoint = ""
    lista_url = getUrl + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 404
    assert_validarResponseSchema(response,cargar_schema("schemaMateria.json")) 

