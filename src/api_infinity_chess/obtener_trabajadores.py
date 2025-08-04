import requests

def obtenerTrabajadores(getUrl):
    endpoint = "obtenerTrabajadores/Modulo 4"
    lista_url = getUrl + endpoint
    response = requests.get(lista_url)
    listaTrabajadores = response.json()
    return listaTrabajadores

def obtenerTrabajadorPorId(getUrl, codigo):
    endpoint = "obtenerTrabajadores/" + codigo
    lista_url = getUrl + endpoint
    response = requests.get(lista_url)
    listaTrabajadores = response.json()
    return listaTrabajadores