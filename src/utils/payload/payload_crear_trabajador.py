from src.utils.generador_codigo import generar_nombre, generar_codigo_trab, generar_fecha_nac, generar_contraseña, generar_fecha_menor, generar_fecha_mayor, generar_fecha_futura

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

