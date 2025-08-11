from src.api_infinity_chess.obtener_curso import obtener_cursos
import requests
from src.utils.payload.payloads_materias import payload_materia_repetida

def existe_materia_repetida(nombre_materia_buscada) -> bool:
    listaMaterias = obtener_cursos("https://backend.clubinfinitychess.com/")
    return any(m["CURSO"] == nombre_materia_buscada for m in listaMaterias)

def crear_materia_repetida(get_Url, endpoint):
    urlFinal = get_Url + endpoint
    response_crear = requests.post(urlFinal, json=payload_materia_repetida)
    assert response_crear.status_code == 201