import re
import pytest
from src.utils.logger_config import logger 

def response_500(response):
     if response.status_code == 500:
          title = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)
          title = title.group(1).strip() if title else "Título no encontrado"
          logger.debug(f"Error 500: {title}.")
          pytest.fail(f"Error 500: {title}.")