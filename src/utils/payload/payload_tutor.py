from src.utils.generador_codigo import generar_cod_inscripcion, generar_nombre,generar_fecha_nac
import random
from datetime import datetime

generos_dic = {
    "Simon": "Hombre",
    "Ander": "Hombre",
    "Andrea": "Mujer",
    "Benjamin": "Hombre",
    "Carmen": "Mujer",
    "Isabel": "Mujer",
    "Raquel": "Mujer",
    "Dylan": "Hombre",
    "Dominic": "Hombre",
}

def determinar_genero(nombre):
    if nombre in generos_dic:
        return generos_dic[nombre]
    if nombre.endswith("a"):
        return "Mujer"
    elif nombre.endswith("o"):
        return "Hombre"
    elif nombre.endswith("e"):
        return "Hombre" if nombre in ["José", "Pepe"] else "Mujer"
    else:
        return "Hombre" 
    
def separar_nombre_completo(nombre_completo,  i):
    partes = nombre_completo.strip().split()
    if len(partes) < 2:
        raise ValueError("Se requiere al menos un nombre y un apellido.")
    return partes[i]

def crear_payload_tutor():
    nombre_completo = generar_nombre()
    cod_tutor = generar_cod_inscripcion(nombre_completo)
    nombre = separar_nombre_completo(nombre_completo,0)
    apellido = separar_nombre_completo(nombre_completo,1)
    fecha_nacimiento = generar_fecha_nac()
    genero = determinar_genero(nombre)
    return {
        "CODTUTOR": cod_tutor,
        "NOMBRETUTOR": nombre,
        "APELLIDOTUTOR": apellido,
        "FECHANACIMIENTOTUTOR": fecha_nacimiento,
        "GENEROTUTOR": genero,
        "CELULARTUTOR": "71234567",
        "CELULARALTERNATIVO": "68751235",
        "CORREO": "prueba@gmail.com",
        "OCUPACION": "Docente"
}

def crear_payload_update_tutor (tutor):
    return {
        "NOMBRETUTOR": tutor["NOMBRETUTOR"] + "E",
        "APELLIDOTUTOR": tutor["APELLIDOTUTOR"] + "E",
        "CELULARTUTOR": "79854123",
}

def crear_payload_update_tutor_nombre (tutor):
    return {
        "NOMBRETUTOR": tutor["NOMBRETUTOR"] + " Editado",
}

def crear_payload_update_tutor_apellido (tutor):
    return {
        "APELLIDOTUTOR": tutor["APELLIDOTUTOR"] + " Editado",
}

def crear_payload_update_tutor_celular (tutor):
    return {
        "CELULARTUTOR": "62998916",
}

def crear_payload_update_nombre_apellido (tutor):
    return {
        "NOMBRETUTOR": tutor["NOMBRETUTOR"] + " Editado",
        "APELLIDOTUTOR": tutor["APELLIDOTUTOR"] + " Editado",
}

def crear_payload_update_nombre_vacio (tutor):
    return {
        "NOMBRETUTOR": "       ",
}

def crear_payload_update_apellido_vacio (tutor):
    return {
        "APELLIDOTUTOR": "       ",
}

def crear_payload_update_numero_vacio (tutor):
    return {
        "CELULARTUTOR": "       ",
}

def crear_payload_update_nombre_caracteres (tutor):
    return {
        "NOMBRETUTOR": "AutomatizacionInteligenteDePruebasSoftwareQAPlussss ",
}

def crear_payload_update_apellido_caracteres (tutor):
    return {
        "APELLIDOTUTOR": "AutomatizacionInteligenteDePruebasSoftwareQAPlussss ",
}

def crear_payload_update_celular_menor_caracteres (tutor):
    return {
        "CELULARTUTOR": "79562",
}

def crear_payload_update_celular_mayor_caracteres (tutor):
    return {
        "CELULARTUTOR": "629845126",
}

def crear_payload_update_celular__caracteres_no_numericos (tutor):
    return {
        "CELULARTUTOR": "pruebaNo",
}

def crear_payload_update_apellido_caracteres_especiales (tutor):
    return {
        "APELLIDOTUTOR": "&#$%&##/&%/#%$%&/()",
}

def crear_payload_update_nombre_caracteres_especiales (tutor):
    return {
        "NOMBRETUTOR": "&#$%&##/&%/#%$%&/()",
}

def crear_payload_update_celular_repetido (tutor):
    return {
        "CELULARTUTOR": "62998916",
}

def crear_payload_update_body_vacio (tutor):
    return {}

def crear_payload_update_nombre_40_caracteres (tutor):
    return {
        "NOMBRETUTOR": "AutomatizacionInteligenteDePruebasSoftwa",
}

def crear_payload_update_apellido_40_caracteres (tutor):
    return {
        "APELLIDOTUTOR": "AutomatizacionInteligenteDePruebasSoftwa",
}

def crear_payload_update_espacios (tutor):
    return {
        "NOMBRETUTOR": " Nombre Espacios ",
        "APELLIDOTUTOR": " Apellido Espacios ",
}

def crear_payload_update_guion_apostrofes (tutor):
    return {
        "NOMBRETUTOR": "Maria-Jose",
        "APELLIDOTUTOR": "O'Connor",
}

def crear_payload_update_cod_pais (tutor):
    return {
        "CELULARTUTOR": "+59162998916",
}