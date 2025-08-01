import requests
import json
import random
import pytest
from src.obtenerCurso import obtenerCodMateria

@pytest.mark.smoke
def test_ObtenerGruposDeUnaMateriaConIdValidoSedeModulo4(getUrl):
    CODMATERIA=obtenerCodMateria(getUrl)
    
    endpoint = "obtenerGrupo/"+CODMATERIA+"/Modulo 4"
    lista_url = getUrl + endpoint
    
    
    headers = {
    'Content-Type': 'application/json'
    }

    #response = requests.request("GET",lista_url, headers=headers)
    response = requests.get(lista_url, headers=headers)
    #para elegir nombre de un grupo
    listaGrupos=response.json()
    #print(response.text)
    assert response.status_code==200
