from src.utils.generador_codigo import generar_nombre, generar_codigo_trab, generar_fecha_nac, generar_contraseña, generar_fecha_menor, generar_fecha_mayor, generar_fecha_futura
from src.api_infinity_chess.obtener_trabajadores import obtener_nombre_de_trabajador

def crear_payload_valido():
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre).strip()
    fecha = generar_fecha_nac()
    contra = generar_contraseña()
    return {
                "CODTRABAJADOR": codigo,
                "NOMBRETRABAJADOR": nombre, 
                "FECHANACIMIENTOTRABAJADOR": fecha, 
                "ROLTRABAJADOR" : "Maestro",
                "CODSEDE": "Modulo 4",
                "CONTRASEÑA": contra,
                }
    
def payload_con_codigo_existente(payload):
    nombre_2 = generar_nombre()
    fecha = generar_fecha_nac()
    contra = generar_contraseña()
    return {
        "CODTRABAJADOR": payload.get("CODTRABAJADOR"),
        "NOMBRETRABAJADOR": nombre_2, 
        "FECHANACIMIENTOTRABAJADOR": fecha, 
        "ROLTRABAJADOR" : "Maestro",
        "CODSEDE": "Modulo 4",
        "CONTRASEÑA": contra,
    }

def payload_con_nombre_existente(payload):
    codigo = generar_codigo_trab()
    fecha = generar_fecha_nac()
    contra = generar_contraseña()
    return {
        "CODTRABAJADOR": codigo,
        "NOMBRETRABAJADOR": payload.get("NOMBRETRABAJADOR"),
        "FECHANACIMIENTOTRABAJADOR": fecha, 
        "ROLTRABAJADOR" : "Maestro",
        "CODSEDE": "Modulo 4",
        "CONTRASEÑA": contra,
    }

def payload_con_nombre_invalido():
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre)
    fecha = generar_fecha_nac()
    contra = generar_contraseña()
    return {
        "CODTRABAJADOR": codigo,
        "NOMBRETRABAJADOR": "123456SAI",
        "FECHANACIMIENTOTRABAJADOR": fecha, 
        "ROLTRABAJADOR" : "Maestro",
        "CODSEDE": "Modulo 4",
        "CONTRASEÑA": contra,
    }

def crear_payload_fecha_menor():
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre).strip()
    fecha = generar_fecha_menor()       #fecha invalida menor a 18 años
    contra = generar_contraseña()
    return {
                "CODTRABAJADOR": codigo,
                "NOMBRETRABAJADOR": nombre, 
                "FECHANACIMIENTOTRABAJADOR": fecha, 
                "ROLTRABAJADOR" : "Maestro",
                "CODSEDE": "Modulo 4",
                "CONTRASEÑA": contra,
                }

def crear_payload_fecha_mayor():
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre).strip()
    fecha = generar_fecha_mayor()       #fecha invalida mayor a 75 años
    contra = generar_contraseña()
    return {
                "CODTRABAJADOR": codigo,
                "NOMBRETRABAJADOR": nombre, 
                "FECHANACIMIENTOTRABAJADOR": fecha, 
                "ROLTRABAJADOR" : "Maestro",
                "CODSEDE": "Modulo 4",
                "CONTRASEÑA": contra,
                }

def crear_payload_fecha_futura():
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre).strip()
    fecha = generar_fecha_futura()       #fecha invalida
    contra = generar_contraseña()
    return {
                "CODTRABAJADOR": codigo,
                "NOMBRETRABAJADOR": nombre, 
                "FECHANACIMIENTOTRABAJADOR": fecha, 
                "ROLTRABAJADOR" : "Maestro",
                "CODSEDE": "Modulo 4",
                "CONTRASEÑA": contra,
                }

def payload_con_rol_invalido():
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre).strip()
    fecha = generar_fecha_nac()
    contra = generar_contraseña()
    return {
                "CODTRABAJADOR": codigo,
                "NOMBRETRABAJADOR": nombre, 
                "FECHANACIMIENTOTRABAJADOR": fecha, 
                "ROLTRABAJADOR" : "Trasnportista",      #rol invalido
                "CODSEDE": "Modulo 4",
                "CONTRASEÑA": contra,
                }

def payload_con_contraseña_corta():
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre).strip()
    fecha = generar_fecha_nac()
    contra = "ABC123"       #contraseña invalida
    return {
                "CODTRABAJADOR": codigo,
                "NOMBRETRABAJADOR": nombre, 
                "FECHANACIMIENTOTRABAJADOR": fecha, 
                "ROLTRABAJADOR" : "Maestro",
                "CODSEDE": "Modulo 4",
                "CONTRASEÑA": contra,
                }

def payload_con_contraseña_vacia():
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre).strip()
    fecha = generar_fecha_nac()
    return {
                "CODTRABAJADOR": codigo,
                "NOMBRETRABAJADOR": nombre, 
                "FECHANACIMIENTOTRABAJADOR": fecha, 
                "ROLTRABAJADOR" : "Maestro",
                "CODSEDE": "Modulo 4",
                "CONTRASEÑA": "",       #contraseña invalida
                }

def payload_con_contraseña_igual_a_nombre():
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre).strip()
    fecha = generar_fecha_nac()
    contra = nombre
    return {
                "CODTRABAJADOR": codigo,
                "NOMBRETRABAJADOR": nombre, 
                "FECHANACIMIENTOTRABAJADOR": fecha, 
                "ROLTRABAJADOR" : "Maestro",
                "CODSEDE": "Modulo 4",
                "CONTRASEÑA": nombre,       #contraseña invalida
                }

def payload_con_contraseña_invalida():
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre).strip()
    fecha = generar_fecha_nac()
    contra = "@@##$$%%!!"       #contraseña invalida
    return {
                "CODTRABAJADOR": codigo,
                "NOMBRETRABAJADOR": nombre, 
                "FECHANACIMIENTOTRABAJADOR": fecha, 
                "ROLTRABAJADOR" : "Maestro",
                "CODSEDE": "Modulo 4",
                "CONTRASEÑA": contra,
                }

def payload_con_campos_vacios():
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre).strip()
    contra = generar_contraseña()
    return {
                "CODTRABAJADOR": codigo,
                "NOMBRETRABAJADOR": nombre, 
                "FECHANACIMIENTOTRABAJADOR": "",        #campo vacio
                "ROLTRABAJADOR" : "",       #campo vacio
                "CODSEDE": "Modulo 4",
                "CONTRASEÑA": contra,
                }

def payload_con_campos_obligatorios_vacios():
    fecha = generar_fecha_nac()
    contra = generar_contraseña()
    return {
                "CODTRABAJADOR": "",        #campo vacio
                "NOMBRETRABAJADOR": "",     #campo vacio
                "FECHANACIMIENTOTRABAJADOR": fecha,
                "ROLTRABAJADOR" : "Maestro",
                "CODSEDE": "Modulo 4",
                "CONTRASEÑA": contra,
                }

def crear_payload_para_actualizar(trabajador):
    nombre = generar_nombre()
    return {
            "NOMBRETRABAJADOR":nombre,
            "FECHANACIMIENTOTRABAJADOR":generar_fecha_nac(),
            "ROLTRABAJADOR" : "Secretarie",
            "CONTRASEÑA": generar_contraseña()
            }

def crear_payload_para_con_campos_vacios(trabajador):
    
    return {
            "NOMBRETRABAJADOR":"",
            "FECHANACIMIENTOTRABAJADOR":generar_fecha_nac(),
            "ROLTRABAJADOR" : "",
            "CONTRASEÑA": ""
            }

def crear_payload_para_actualizar_CODTRABAJADOR(trabajador):
    return {
            "CODTRABAJADOR":"789654CODIG"
            }

def crear_payload_para_actualizar_NOMBRETRABAJADOR(trabajador):
    return {
            "NOMBRETRABAJADOR":"9876543210"
            }

def crear_payload_para_actualizar_NOMBRETRABAJADOR_repetido(trabajador_2):
    return {
            "NOMBRETRABAJADOR":trabajador_2
            }

def crear_payload_para_actualizar_fecha_menor(trabajador):
    fecha = generar_fecha_menor()
    return {
            "FECHANACIMIENTOTRABAJADOR":fecha
            }

def crear_payload_para_actualizar_fecha_mayor(trabajador):
    fecha = generar_fecha_mayor()
    return {
            "FECHANACIMIENTOTRABAJADOR":fecha
            }

def crear_payload_para_actualizar_rol(trabajador):
    return {
            "ROLTRABAJADOR":"Peluquero"
            }

def crear_payload_para_contra_sin_numeros(trabajador):
    return {
            "CONTRASEÑA":"QSC$$!!//~@"
            }

def crear_payload_para_contra_corta(trabajador):
    return {
            "CONTRASEÑA":"123ABC"
            }

def crear_payload_para_contra_vacia(trabajador):
    return {
            "CONTRASEÑA":""
            }

def crear_payload_para_contra_igual_a_nombre(nombre):
    return {
            "CONTRASEÑA":nombre
            }

def crear_payload_vacio(trabajador):
    
    return {
            
            }

def crear_payload_para_actualizar_E2E(trabajador):
    nombre = generar_nombre()
    return {
            "NOMBRETRABAJADOR":nombre,
            "FECHANACIMIENTOTRABAJADOR":generar_fecha_nac(),
            "ROLTRABAJADOR" : "Secretarie",
            "CONTRASEÑA": generar_contraseña()
            }