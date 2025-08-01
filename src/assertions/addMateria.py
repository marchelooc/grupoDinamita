import json
import os
import jsonschema
import pytest

# Ruta absoluta al archivo JSON
schema_path = os.path.join(os.path.dirname(__file__), "../utils/schemas/schemaMateria.json")

# Cargar el schema
with open(schema_path, "r", encoding="utf-8") as f:
    schemaMateria = json.load(f)

def assert_crearMateriaSchema(response):
    try:
        jsonschema.validate(instance=response.json(), schema=schemaMateria)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema doesn't match: {err.message}")