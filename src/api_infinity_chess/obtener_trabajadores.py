import requests

def obtener_trabajadores(get_url):
    endpoint = "obtenerTrabajadores/Modulo 4"
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    lista_trabajadores = response.json()
    return lista_trabajadores

def obtener_trabajador_por_Id(get_url, codigo):
    endpoint = "obtenerTrabajadores/" + codigo
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    lista_trabajadores = response.json()
    return lista_trabajadores