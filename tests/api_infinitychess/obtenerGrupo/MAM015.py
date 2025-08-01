import requests
import json
import random
from src import obtenerCurso

def ObtenerGruposDeUnaMateriaConIdValidoSedeModulo4(getUrl):
    endpoint = "obtenerGrupp/"+CODMATERIA+"/Modulo 4"
    lista_url = getUrl + endpoint
    
    cursos=obtenerCurso(getUrl)
    CODMATERIA = random.choice(cursos)["CODCURSO"]
    

    headers = {
    'Content-Type': 'application/json'
    }

    #response = requests.request("GET",lista_url, headers=headers)
    response = requests.get(lista_url, headers=headers)
    #para elegir nombre de un grupo
    listaGrupos=response.json()
    #print(response.text)
    assert response.status_code==200
