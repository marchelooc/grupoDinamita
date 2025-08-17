from src.utils.generador_codigo import generar_nom_materia, generar_cod


payload_materia_correcta = {
    "CODCURSO": "2025Taller",
    "CURSO": "Taller" ,
    "ESTADO": "activo",
    }

def generar_materia_aleatoria():
    nombre_curso = generar_nom_materia()
    codigo_curso = generar_cod (nombre_curso)
    payload_materia_aleatoria = {
                    "CODCURSO": codigo_curso,
                    "CURSO": nombre_curso,
                    "ESTADO": "activo",
                    }
    return payload_materia_aleatoria

payload_materia_vacia = {
                "CODCURSO": "",
                "CURSO": "",
                "ESTADO": "",
                }
payload_materia_sin_CODCURSO = {
                "CODCURSO": "",
                "CURSO": "Mecatronica", 
                "ESTADO": "activo",
                }
payload_materia_sin_Nombre = {
                "CODCURSO": "2025BIOLOGIA",
                "CURSO": "", 
                "ESTADO": "activo",
                }
payload_materia_repetida = {
                "CODCURSO": "123Mrepetida",
                "CURSO": "MateriaRepetida",
                "ESTADO": "activo",
                }
payload_materia_CONDCURSO_largo = {
                "CODCURSO": "2025ARITMETICA_AVANZADA",
                "CURSO": "ARITMETICA_AVANZADA", 
                "ESTADO": "activo",
                }
payload_materia_nombre_largo = {
                "CODCURSO": "2025CAPORALES",
                "CURSO": "CURSO DE CAPORALES ORUREÑO DE LARGO ALCANSE EN BOLIVIA", 
                "ESTADO": "activo",
                }
payload_materia_CODCURSO_invalido = {
                "CODCURSO":"2025$UM@",
                "CURSO": "SUMA", 
                "ESTADO": "activo",
                }
payload_materia_nombre_invalido = {
                "CODCURSO":"2025SOCIALES",
                "CURSO": "$o$&@le$", 
                "ESTADO": "activo",
                }
payload_materia_a_eliminar = {
                "CODCURSO":"2025MECA",
                "CURSO": "eliminar Mecatronica", 
                "ESTADO": "activo",
                }
payload_materia_nombre_similar1 = {
                "CODCURSO":"REPE1",
                "CURSO": "FilosofiaREP", 
                "ESTADO": "activo",
                }
payload_materia_nombre_similar2 = {
                "CODCURSO":"REPE2",
                "CURSO": "FilosofiaREP", 
                "ESTADO": "activo",
                }

headers_json = {
            "Accept": "application/json",
            "Content-Type": "application/json"
    }
headers_text = {
            "Accept": "application/json",
            "Content-Type": "text/plain",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)"
    }