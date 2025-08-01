import jsonschema
import pytest

def assert_validarResponseSchema(response, schema):
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"El JSON no coincide con el esquema: {err.message}")

def assert_validarSchemaInput(data, schema,contexto=""):
    try:
        jsonschema.validate(instance=data, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        mensaje = f"JSON no válido en contexto '{contexto}': {err.message}"
        pytest.fail(mensaje)