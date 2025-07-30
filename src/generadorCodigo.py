import random
import string

def generarCodigo():
    numero = str(random.randint(100000, 999999))
    letras = ''.join(random.choices(string.ascii_uppercase, k=6))
    return numero + letras
