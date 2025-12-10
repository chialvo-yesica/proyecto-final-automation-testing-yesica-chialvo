from datetime import datetime
from pathlib import Path
from selenium.webdriver.remote.webdriver import WebDriver

from config.settings import SCREENSHOTS_FOLDER

#Guarda una captura de pantalla en la carpeta configurada. El nombre incluye el nombre del test y la fecha/hora.
def capture_screenshot(web_driver: WebDriver, test_id: str) -> Path:
    current_time_str = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    safe_test_id = test_id.replace("test_", "").replace(" ", "_").replace("[", "_").replace("]", "")
    screenshot_name = f"FAIL_{safe_test_id}_{current_time_str}.png" 
    output_path = SCREENSHOTS_FOLDER / screenshot_name

    # Se guarda el screenshot en la ruta indicada
    web_driver.save_screenshot(str(output_path))

    return output_path