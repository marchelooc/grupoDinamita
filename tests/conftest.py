import pytest
from config import get_base_url
import os
from dotenv import load_dotenv
import sys

load_dotenv()

py_path = os.getenv("PYTHONPATH")
if py_path and py_path not in sys.path:
    sys.path.insert(0, py_path)

@pytest.fixture
def get_url():
    return get_base_url()

def pytest_collection_modifyitems(config, items):
    marker_expr = config.getoption("-m")
    if marker_expr == "regression":
        # Ignora el filtro de marcadores, ejecuta todos
        config.option.markexpr = ""
