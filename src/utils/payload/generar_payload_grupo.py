
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