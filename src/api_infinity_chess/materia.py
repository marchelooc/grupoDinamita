from src.api_infinity_chess.obtener_curso import obtener_cursos
import requests

def existe_materia_repetida(getUrl) -> bool:
    nombre_materia_buscada = "MateriaRepetida"
    listaMaterias = obtener_cursos(getUrl)
    return any(m["CURSO"] == nombre_materia_buscada for m in listaMaterias)

def crear_materia_repetida(get_Url, endpoint):
    payload = {
                "CODCURSO": "123Mrepetida",
                "CURSO": "MateriaRepetida",
                "ESTADO": "activo",
                }
    urlFinal = get_Url + endpoint
    response_crear = requests.post(urlFinal, json=payload)
    assert response_crear.status_code == 201