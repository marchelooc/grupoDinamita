import jsonschema
import pytest

def assert_validarResponseSchema(response, schema):
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"El JSON no coincide con el esquema: {err.message}")
