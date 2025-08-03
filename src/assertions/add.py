import jsonschema
import pytest
from src.utils.logger_config import logger 

def assert_validar_response_schema(response, schema):
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
        logger.info("Schema validado correctamente.")
        return True
    except jsonschema.exceptions.ValidationError as err:
        logger.info("El JSON no coincide con el esquema: {err.message}")
        pytest.fail(f"El JSON no coincide con el esquema: {err.message}")

def assert_validar_schema_input(data, schema,contexto=""):
    try:
        jsonschema.validate(instance=data, schema=schema)
        logger.info("Schema validado correctamente.")
        return True
    except jsonschema.exceptions.ValidationError as err:
        logger.info("El JSON no coincide con el esquema: {err.message}")
        pytest.fail(f"El JSON no coincide con el esquema: {err.message}")