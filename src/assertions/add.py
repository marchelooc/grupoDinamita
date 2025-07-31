import json
import os
import jsonschema
import pytest

# Ruta absoluta al archivo JSON
schema_path = os.path.join(os.path.dirname(__file__), "../utils/schemaGrupo.json")

# Cargar el schema
with open(schema_path, "r", encoding="utf-8") as f:
    schemaGrupo = json.load(f)

def assert_crearGrupoSchema(response):
    try:
        jsonschema.validate(instance=response.json(), schema=schemaGrupo)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema doesn't match: {err.message}")