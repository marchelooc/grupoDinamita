import requests

def obtener_tutores_activos(get_url):
    endpoint = "obtenerTutoresActivos"
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    lista_tutores = response.json()
    return lista_tutores

def obtener_tutores_inactivos(get_url):
    endpoint = "obtenerTutoresInactivos"
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    lista_tutores = response.json()
    return lista_tutores
