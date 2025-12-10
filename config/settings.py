import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Se define REPORTS_FOLDER y SCREENSHOTS_FOLDER (dentro de reports)
REPORTS_FOLDER = PROJECT_ROOT / "reports"
SCREENSHOTS_FOLDER = REPORTS_FOLDER / "screenshots" 

# Se crean los directorios si no existen
for path in (REPORTS_FOLDER, SCREENSHOTS_FOLDER):
    path.mkdir(parents=True, exist_ok=True)

BASE_URL_WEB = "https://www.saucedemo.com"
BASE_URL_API_SERVICE = "https://jsonplaceholder.typicode.com"

TEST_BROWSER = os.getenv("TEST_BROWSER", "chrome")

# Tiempos de espera (en segundos)
WAIT_IMPLICIT = 10 
TIMEOUT_PAGE_LOAD = 30