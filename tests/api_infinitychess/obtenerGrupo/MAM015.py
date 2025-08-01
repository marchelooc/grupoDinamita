import requests
import json
import random
from src.api_infinityChess.obtenerCurso import obtenerCursos

def ObtenerGruposDeUnaMateriaConIdValidoSedeModulo4(getUrl):
    endpoint = "obtenerGrupp/"+CODMATERIA+"/Modulo 4"
    lista_url = getUrl + endpoint
    
    cursos=obtenerCursos(getUrl)
    CODMATERIA = random.choice(cursos)["CODCURSO"]
    

    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("GET", lista_url, headers=headers)

    #print(response.text)
    assert response.status_code==200
    
