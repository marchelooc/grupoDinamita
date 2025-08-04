import requests

def obtenerTutoresActivos(getUrl):
    endpoint = "obtenerTutoresActivos"
    lista_url = getUrl + endpoint
    response = requests.get(lista_url)
    listaTutores = response.json()
    return listaTutores

def obtenerTutoresInactivos(getUrl):
    endpoint = "obtenerTutoresInactivos"
    lista_url = getUrl + endpoint
    response = requests.get(lista_url)
    listaTutores = response.json()
    return listaTutores
