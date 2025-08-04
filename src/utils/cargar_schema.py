import json
import os

def cargar_schema(nombre_archivo):
    ruta = os.path.join(os.path.dirname(__file__), "../utils/schemas/", nombre_archivo)
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)
