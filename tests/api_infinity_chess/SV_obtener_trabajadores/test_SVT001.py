import requests
import pytest
import random
from src.api_infinity_chess.obtener_trabajadores import obtener_trabajadores

@pytest.mark.smoke
def test_obtener_trabajador_existente_porId_valido(get_url):
    lista_trabajdores = obtener_trabajadores(get_url)
    CODTRABAJADOR = random.choice(lista_trabajdores)["CODTRABAJADOR"]
    print(f"Trabajador escogido es: {CODTRABAJADOR}")
    endpoint = "obtenerTrabajadores/" + CODTRABAJADOR
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 200
    #print (response.json[0].get("NOMBRETRABAJADOR")) 
    