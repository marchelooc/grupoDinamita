import json
import os
import jsonschema
import pytest

# Ruta absoluta al archivo JSON
schema_path = os.path.join(os.path.dirname(__file__), "../utils/schemaTrabajador.json")

# Cargar el schema
with open(schema_path, "r", encoding="utf-8") as f:
    schemaTrabajador = json.load(f)

def assert_crearTrabajadorSchema(response):
    try:
        jsonschema.validate(instance=response.json(), schema=schemaTrabajador)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema doesn't match: {err.message}")