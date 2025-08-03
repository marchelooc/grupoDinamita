import requests
import pytest
from src.assertions.add import assert_validarResponseSchema,assert_validarSchemaInput
from src.utils.cargarSchema import cargar_schema
from src.api_infinityChess.materia import existeMateriaRepetida, crear_materia_repetida

@pytest.mark.smoke
def test_validar_comportamiento_al_agregar_curso_con_CODCURSO_duplicado(get_url):
    endpoint = "agregarCurso"

    payload = {
                "CODCURSO": "123Mrepetida",
                "CURSO": "MateriaRepetida",
                "ESTADO": "activo",
                }
    
    if not existeMateriaRepetida(get_url):
        crear_materia_repetida(get_url, endpoint)
        
    assert_validarSchemaInput(payload,cargar_schema("schema_materia.json"))
    urlFinal = get_url + endpoint
    response = requests.post(urlFinal, json=payload)
    assert response.status_code == 500
    #assert_validarResponseSchema(response,cargar_schema("schema_materia.json")) 
    
