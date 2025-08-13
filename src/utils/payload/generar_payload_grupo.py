from src.utils.generador_codigo import obtener_nombre_grupo, generar_cod, obtener_dias, obtener_horas, obtener_limite, obtener_precio, obtener_nombre_grupo_2_caracteres, obtener_nombre_grupo_3_caracteres

def generar_payload_completo(CODCURSO):
    nombre_grupo=obtener_nombre_grupo()
    dias=obtener_dias()
    horas=obtener_horas()
    precio=obtener_precio()
    limite=obtener_limite()
    codigo=generar_cod(nombre_grupo)
    payload=cargar_payload_grupo(CODCURSO,nombre_grupo,dias,horas,precio,limite,codigo)
    return payload

def generar_payload_2_carac(CODCURSO):
    nombre_grupo=obtener_nombre_grupo_2_caracteres()
    dias=obtener_dias()
    horas=obtener_horas()
    precio=obtener_precio()
    limite=obtener_limite()
    codigo=generar_cod(nombre_grupo)
    payload=cargar_payload_grupo(CODCURSO,nombre_grupo,dias,horas,precio,limite,codigo)
    return payload

def generar_payload_limite(CODCURSO):
    nombre_grupo=obtener_nombre_grupo()
    dias=obtener_dias()
    horas=obtener_horas()
    precio=obtener_precio()
    codigo=generar_cod(nombre_grupo)
    payload = cargar_payload_grupo(CODCURSO,nombre_grupo,dias,horas,precio,0,codigo)
    return payload

def generar_payload_nom_largo(CODCURSO):
    nombre_grupo="Este es el nombre de grupo con muy largo"
    dias=obtener_dias()
    horas=obtener_horas()
    precio=obtener_precio()
    limite=obtener_limite()
    codigo=generar_cod(nombre_grupo)
    payload = cargar_payload_grupo(CODCURSO,nombre_grupo,dias,horas,precio,limite,codigo)
    return payload

def generar_payload_horario_invalido(CODCURSO):
    nombre_grupo=obtener_nombre_grupo()
    dias=obtener_dias()
    precio=obtener_precio()
    limite=obtener_limite()
    codigo=generar_cod(nombre_grupo)
    payload = cargar_payload_grupo(CODCURSO,nombre_grupo,dias,"23:00",precio,limite,codigo)
    return payload

def generar_payload_precio(CODCURSO):
    nombre_grupo=obtener_nombre_grupo()
    dias=obtener_dias()
    horas=obtener_horas()
    limite=obtener_limite()
    codigo=generar_cod(nombre_grupo)
    payload = cargar_payload_grupo(CODCURSO,nombre_grupo,dias,horas,0,limite,codigo)
    return payload

def generar_payload_3_carac(CODCURSO):
    nombre_grupo=obtener_nombre_grupo_3_caracteres()
    dias=obtener_dias()
    horas=obtener_horas()
    precio=obtener_precio()
    limite=obtener_limite()
    codigo=generar_cod(nombre_grupo)
    payload = cargar_payload_grupo(CODCURSO,nombre_grupo,dias,horas,precio,limite,codigo)
    return payload

def generar_payload_duplicado(CODCURSO,nombre_grupo):
    dias=obtener_dias()
    horas=obtener_horas()
    precio=obtener_precio()
    limite=obtener_limite()
    codigo=generar_cod(nombre_grupo)
    payload= cargar_payload_grupo(CODCURSO,nombre_grupo,dias,horas,precio,limite,codigo)
    return payload

def generar_payload_eliminar(CODCURSO,nombre_grupo,codigo):
    dias=obtener_dias()
    horas=obtener_horas()
    precio=obtener_precio()
    limite=obtener_limite()
    payload=cargar_payload_grupo(CODCURSO,nombre_grupo,dias,horas,precio,limite,codigo)    
    return payload

def generar_payload_limite(CODMATERIA,nombre_grupo,codigo,limite):
    dias=obtener_dias()
    horas=obtener_horas()
    precio=obtener_precio()
    payload=cargar_payload_grupo(CODMATERIA,nombre_grupo,dias,horas,precio,limite,codigo)
    return payload

def cargar_payload_grupo(CODCURSO,nombre_grupo,dias,horas,precio,limite,codigo):
    payload = {
        "CODCURSO": CODCURSO,
        "CODSEDE": "Modulo 4",
        "NOMBREGRUPO": nombre_grupo, 
        "CODGRUPO": codigo,
        "LIMITE" :limite,
        "PRECIO":precio,
        "DIAS" : dias,
        "HORA":horas} 
    return payload