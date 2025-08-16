from datetime import date, timedelta
import random
from src.api_infinity_chess.obtener_tutores import obtener_tutores_activos

def crear_payload_motivo_exitoso (get_url):
    lista_tutores = obtener_tutores_activos(get_url)
    cod_tutor = random.choice(lista_tutores)["CODTUTOR"]
    return {
        "CODTUTOR": cod_tutor, 
        "MOTIVO": "Prueba", 
        "FECHAMOTIVO": date.today().strftime("%d/%m/%Y"), 
        "ESTADO": "Activo"
    }

def crear_payload_motivo_campos_vacios ():
    return {
        "CODTUTOR": "", 
        "MOTIVO": "", 
        "FECHAMOTIVO": "", 
        "ESTADO": ""
    }

def crear_payload_motivo_fecha_formato_incorrecto (get_url):
    lista_tutores = obtener_tutores_activos(get_url)
    cod_tutor = random.choice(lista_tutores)["CODTUTOR"]
    return {
        "CODTUTOR": cod_tutor, 
        "MOTIVO": "Prueba fecha formato incorrecto", 
        "FECHAMOTIVO": "ASDFASDF", 
        "ESTADO": "Activo"
    }

def crear_payload_motivo_tutor_inexistente ():
    return {
        "CODTUTOR": "AASDKJEKJIWER", 
        "MOTIVO": "Prueba tutor inexistente", 
        "FECHAMOTIVO": date.today().strftime("%d/%m/%Y"), 
        "ESTADO": "Activo"
    }

def crear_payload_motivo_estado_inactivo (get_url):
    lista_tutores = obtener_tutores_activos(get_url)
    cod_tutor = random.choice(lista_tutores)["CODTUTOR"]
    return {
        "CODTUTOR": cod_tutor, 
        "MOTIVO": "Prueba campo estado inactivo", 
        "FECHAMOTIVO": date.today().strftime("%d/%m/%Y"), 
        "ESTADO": "Inactivo"
    }

def crear_payload_motivo_estado_activo (get_url):
    lista_tutores = obtener_tutores_activos(get_url)
    cod_tutor = random.choice(lista_tutores)["CODTUTOR"]
    return {
        "CODTUTOR": cod_tutor, 
        "MOTIVO": "Prueba campo estado activo", 
        "FECHAMOTIVO": date.today().strftime("%d/%m/%Y"), 
        "ESTADO": "Activo"
    }

def crear_payload_motivo_fecha_futura (get_url):
    lista_tutores = obtener_tutores_activos(get_url)
    cod_tutor = random.choice(lista_tutores)["CODTUTOR"]
    fecha_futura = (date.today() + timedelta(days=5)).strftime("%d/%m/%Y")
    return {
        "CODTUTOR": cod_tutor, 
        "MOTIVO": "Prueba motivo con fecha futua", 
        "FECHAMOTIVO": fecha_futura, 
        "ESTADO": "Activo"
    }

def crear_payload_motivo_tutor_vacio ():
    return {
        "CODTUTOR": "" , 
        "MOTIVO": "Prueba crear motivo con tutor vacio", 
        "FECHAMOTIVO": date.today().strftime("%d/%m/%Y"), 
        "ESTADO": "Activo"
    }


def crear_payload_motivo_largo (get_url):
    lista_tutores = obtener_tutores_activos(get_url)
    cod_tutor = random.choice(lista_tutores)["CODTUTOR"]
    return {
        "CODTUTOR": cod_tutor , 
        "MOTIVO": "123456789012345678901234567890123456789012345678901", 
        "FECHAMOTIVO": date.today().strftime("%d/%m/%Y"), 
        "ESTADO": "Activo"
    }

def crear_payload_motivo_fecha_vacia (get_url):
    lista_tutores = obtener_tutores_activos(get_url)
    cod_tutor = random.choice(lista_tutores)["CODTUTOR"]
    return {
        "CODTUTOR": cod_tutor , 
        "MOTIVO": "motivo prueba", 
        "FECHAMOTIVO": "", 
        "ESTADO": "Activo"
    }

def crear_payload_motivo_fecha_antigua (get_url):
    lista_tutores = obtener_tutores_activos(get_url)
    cod_tutor = random.choice(lista_tutores)["CODTUTOR"]
    fecha_antigua = (date.today() - timedelta(days=50000)).strftime("%d/%m/%Y") 
    return {
        "CODTUTOR": cod_tutor, 
        "MOTIVO": "Motivo con fecha antigua", 
        "FECHAMOTIVO": fecha_antigua, 
        "ESTADO": "Activo"
    }

def crear_payload_motivo_50_caracteres (get_url):
    lista_tutores = obtener_tutores_activos(get_url)
    cod_tutor = random.choice(lista_tutores)["CODTUTOR"] 
    return {
        "CODTUTOR": cod_tutor , 
        "MOTIVO": "12345678901234567890123456789012345678901234567890", 
        "FECHAMOTIVO": date.today().strftime("%d/%m/%Y"), 
        "ESTADO": "Activo"
    }

def crear_payload_motivo_vacio (get_url):
    lista_tutores = obtener_tutores_activos(get_url)
    cod_tutor = random.choice(lista_tutores)["CODTUTOR"] 
    return {
        "CODTUTOR": cod_tutor , 
        "MOTIVO": "", 
        "FECHAMOTIVO": date.today().strftime("%d/%m/%Y"), 
        "ESTADO": "Activo"
    }