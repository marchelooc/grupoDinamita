from datetime import datetime, timedelta
from src.api_infinity_chess.materia import existe_materia_repetida
import random
import string

def generar_codigo():
    numero = str(random.randint(100000, 999999))
    letras = ''.join(random.choices(string.ascii_uppercase, k=6))
    return numero + letras
 
def obtener_nombre_grupo():
    grupos = ["Grupo1", "Grupo2", "Grupo3", "Grupo4", "Grupo5","Grupo6", "Grupo7", "Grupo8", "Grupo9", "Grupo10",
            "Grupo11", "Grupo12", "Grupo13", "Grupo14", "Grupo15","Grupo16", "Grupo17", "Grupo18", "Grupo19", "Grupo20"]
    return random.choice(grupos)

def obtener_dias():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes","Sabado"]
    cantidad = random.randint(1, 6)
    lista_de_dias = random.sample(dias, cantidad)
    return lista_de_dias

def obtener_horas():
    horas = ["06:00","07:00", "08:00", "09:00", "10:00", "11:00","12:00","13:00","14:00","15:00","16:00",
            "17:00","18:00","19:00","20:00","21:00"]
    return random.choice(horas)

def obtener_limite():
    limite=random.randint(1,30)
    return limite

def obtener_precio():
    precio=random.randint(1,100)
    return precio


def generar_cod (cod):
    año = datetime.now().year
    return f"{año}{cod}"

def generar_cod_inscripcion(nombre_completo):
    partes = nombre_completo.strip().split()
    if len(partes) < 2:
        raise ValueError("Se requiere al menos un nombre y un apellido.")
    nombre = partes[0]
    apellido = partes[1]
    sub_nombre = nombre[:3]
    sub_apellido = apellido[:3]
    ahora = datetime.now()
    año = ahora.year
    mes = ahora.month
    dia = ahora.day
    codigo = f"{año}{mes:02}{dia:02}{sub_nombre}{sub_apellido}"
    return codigo.upper()

def generar_codigo_trab(nombre: str) -> str:
    fechaHoy = datetime.now().strftime("%Y%m%d")  
    return f"{fechaHoy}{nombre[:5].upper()}"

def generar_nombre():
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    return f"{nombre} {apellido}"
    
    
nombres = [
    "Carlos", "María", "Ana", "Luis", "José", "Lucía", "Simon", "Ander", "Raquel", "Omar", "Brayan",
    "Pedro", "Camila", "Andrés", "Valeria", "Diego", "Fernanda", "Adriana", "Micaela", "Benjamin",
    "Carmen", "Isabel", "Laura", "Marta", "Patricia", "Sandra", "Sofía", "Karina", "Ernesto",
    "Antonio", "Juan", "Miguel", "Francisco", "Javier", "Fernando", "Santos", "Marcelo", "Pepe",
    "David", "Manuel", "Alejandro", "Rosa", "Elena", "Julia", "Teresa", "Eva", "Beatriz", "Gloria",
    "Raúl", "Jorge", "Sergio", "Pablo", "Alberto", "Álvaro", "Marcos", "Rubén", "Clara", "Luna",
    "Paula", "Valentina", "Andrea", "Gabriela", "Lorena", "Miriam", "Natalia", "Olga", "Aurora",
    "Dylan", "Dominic", "Leonel", "Ronaldo", "Bladimir", "Estela", "Cristina", "Amanda", "Zenaida",
]

apellidos = [
    "Pérez", "Gómez", "Rodríguez", "Martínez", "López",
    "Sánchez", "Gutiérrez", "Ramírez", "Torres", "Vargas",
    "Fernández", "Jiménez", "Ruiz", "Díaz", "Moreno",
    "Muñoz", "Álvarez", "Romero", "Alonso", "Herrera",
    "Castro", "Ortiz", "Delgado", "Navarro", "Rojas",
    "Mendoza", "Castillo", "Flores", "Silva", "Cruz",
    "Suárez", "Ramos", "Reyes", "Molina", "Ortega",
    "Aguilar", "Pineda", "Aguirre", "Carrasco", "Cárdenas",
    "Campos", "Fuentes", "Salazar", "Santana", "Medina",
    "Guerrero", "Camacho", "Márquez", "Ibarra", "Valencia"
]    

def generar_fecha_nac(edad_min=18, edad_max=75):
    hoy = datetime.today()
    dias_min = edad_min * 365
    dias_max = edad_max * 365
    dias_random = random.randint(dias_min, dias_max)
    fecha_nacimiento = hoy - timedelta(days=dias_random)
    return fecha_nacimiento.strftime("%Y-%m-%d")

def generar_fecha_menor():      # Generar una fecha de nacimiento menor a 18 años
    hoy = datetime.today()
    fecha_menor = hoy - timedelta(days=16 * 365)
    return fecha_menor.strftime('%Y-%m-%d')

def generar_fecha_mayor():      # Generar una fecha de nacimiento mayor a 75 años
    hoy = datetime.today()
    fecha_mayor = hoy - timedelta(days=78 * 365)
    return fecha_mayor.strftime('%Y-%m-%d')

def generar_fecha_futura(start_year=2033, end_year=2100):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta_days = (end - start).days
    random_days = random.randint(0, delta_days)
    fecha = start + timedelta(days=random_days)
    return fecha.strftime('%Y-%m-%d')
    

def generar_contraseña(longitud=10, usar_mayusculas=True, usar_numeros=True):
    caracteres = string.ascii_lowercase 
    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def generar_nom_materia():
    materias = [
            "Ruso", "Esñaol", "Quechua", "Mandarín","Polaco", "Árabe", "Birmano",
            "Chino", "Yoruba", "Japones", "Indonesio", "Portugues","Frances", "Italiano",
            "Ruso2", "Español2", "Quechua2", "Mandarín2","Polaco2", "Árabe2", "Birmano2",
            "Chino2", "Yoruba2", "Japones2", "Indones2", "Portugal2","Frances2", "Italiano2"
            ]
    materia = random.choice(materias)
    existe = existe_materia_repetida(materia)
    if (existe) : 
        while (existe):
            materia = random.choice(materias)
            existe = existe_materia_repetida(materia)
    return materia

def obtener_nombre_grupo_2_caracteres():
    grupos = ["AA", "Ba", "CC", "De", "EE","FF", "GG", "HH", "II", "MM",
            "NN", "12", "34", "GH", "ZZ","LL", "RR", "PP", "QQ", "JJ", "KK", "KL"]
    return random.choice(grupos)

def obtener_nombre_grupo_3_caracteres():
    grupos = ["AAa", "Bat", "CCf", "Deh", "EEc","FFh", "GGi", "HoH", "IaI", "MeM",
            "NN", "1f2", "3r4", "GHi", "ZcZ","LmL", "RvR", "PrP", "QuQ", "JoJ", "KaK", "KiL"]
    return random.choice(grupos)

def generar_cod_caracteres():
    caracteres_especiales = string.punctuation
    codigo = ''.join(random.choice(caracteres_especiales) for _ in range(10))
    return f'"{codigo}"'