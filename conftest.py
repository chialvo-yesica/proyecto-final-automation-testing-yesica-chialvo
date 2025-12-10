import pytest

from utils.driver_factory import initialize_driver
from utils.api_client import RestApiClient
from utils.logger import setup_logger
from utils.screenshot import capture_screenshot

test_logger = setup_logger(log_name="test_runner") # Nombre del logger cambiado

#Agrega opciones de línea de comandos para pytest
def pytest_addoption(parser):
    parser.addoption(
        "--run-headless",
        action="store_true",
        default=False,
        help="Ejecuta los tests de UI en modo headless (sin ventana visible).",
    )

#Fixture de sesión para el cliente de API REST
@pytest.fixture(scope="session")
def rest_client(): 
    test_logger.info("Inicializando RestApiClient para pruebas de servicio.")
    return RestApiClient()

#Fixture para crear y cerrar el WebDriver
@pytest.fixture
def web_driver(request): 
    is_headless = request.config.getoption("--run-headless")
    test_logger.info("Creando instancia de WebDriver (headless=%s).", is_headless)
    driver_instance = initialize_driver(is_headless=is_headless)

    yield driver_instance

    test_logger.info("Cerrando instancia de WebDriver.")
    driver_instance.quit()

#Hook que se ejecuta después de cada fase del test para manejo de screenshots
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Captura solo en fallos de la fase de ejecución y si usa la fixture de UI
    if report.when == "call" and report.failed and "web_driver" in item.fixturenames:
        current_driver = item.funcargs.get("web_driver")
        
        if current_driver is not None:
            test_logger.error("¡Fallo! Test '%s'. Tomando captura.", item.name)
            screenshot_path = capture_screenshot(current_driver, item.name)
            test_logger.error("Captura guardada en: %s", screenshot_path)

            # Adjuntar al reporte HTML
            html_plugin = item.config.pluginmanager.getplugin("html")
            if html_plugin is not None:
                extra_data = getattr(report, "extra", [])
                extra_data.append(html_plugin.extras.png(str(screenshot_path)))
                report.extra = extra_data
        
    # Guardar el reporte para futuros hooks
    if report.when == "call":
        setattr(item, "final_report", report)

#Configuración inicial de pytest
def pytest_configure(config):
    test_logger.info("Inicializando configuración global de Pytest.")