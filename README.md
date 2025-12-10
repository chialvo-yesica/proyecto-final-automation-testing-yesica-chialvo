# Proyecto de Automatización QA: Yesica Chialvo

Este proyecto implementa un framework de automatización de pruebas para validar tanto la interfaz de usuario (UI) como los servicios API de backend. Utiliza Pytest como runner principal, Selenium para las pruebas web y la librería `requests` para las pruebas de API REST.

---

## Proposito del Proyecto

El objetivo principal de este proyecto es garantizar la calidad y funcionalidad de una aplicación web y sus servicios asociados a través de pruebas automatizadas:

1.  **Validación UI (Web):** Verificar el flujo crítico de usuarios en la plataforma de comercio electrónico **SauceDemo**, incluyendo la autenticación (positiva y negativa), el manejo del carrito de compras y el flujo completo de compra (end-to-end).
2.  **Validación API (Servicios REST):** Confirmar la correcta interacción con un servicio REST externo (JSONPlaceholder) para las operaciones fundamentales (GET, POST, DELETE).
3.  **Mantenibilidad:** Aplicar el patrón Page Object Model (POM) para mantener el código de prueba limpio, legible y fácil de mantener a largo plazo.

---

## Tecnologias Utilizadas

| Categoria | Tecnologia | Version Requerida | Proposito |
| :--- | :--- | :--- | :--- |
| **Lenguaje** | Python | 3.10+ | Lenguaje de desarrollo principal. |
| **Test Runner** | Pytest | Ultima | Ejecución, descubrimiento y gestión de pruebas. |
| **Web UI** | Selenium WebDriver | Ultima | Interacción con la interfaz web (Browser Automation). |
| **API Testing** | `requests` | Ultima | Cliente HTTP para enviar peticiones REST. |
| **Reporting** | `pytest-html` | Ultima | Generación de reportes detallados en formato HTML. |

---

## Estructura del Proyecto

La estructura sigue un diseño modular y organizado, separando la configuración, las páginas web, los tests y las utilidades.

```bash
proyecto-final-automation-testing-yesica-chialvo/
├─ config/
│  └─ settings.py          
├─ data/
│  └─ login_auth_errors.json
├─ pages/                 
│  ├─ base_page.py         
│  ├─ cart_page.py 
│  ├─ checkout_page.py 
│  ├─ inventory_page.py 
│  └─ login_page.py
├─ tests/
│  ├─ api/  
│  │  ├─ test_rest_delete.py
│  │  ├─ test_rest_get.py
│  │  └─ test_rest_post.py
│  └─ ui/ 
│     ├─ test_auth_negative.py
│     ├─ test_auth_positive.py
│     ├─ test_cart_flow.py
│     └─ test_purchase_flow.py
├─ utils/
│  ├─ api_client.py
│  ├─ data_reader.py
│  ├─ driver_factory.py
│  ├─ logger.py
│  └─ screenshot.py
├─ conftest.py
├─ pytest.ini
├─ README.md
└─ requirements.txt
```
---

## Como Instalar las Dependencias

Asegurate de tener **Python 3.10 o superior** instalado en tu sistema.

1.  **Instalar las dependencias** listadas en `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
2.  **WebDriver:** Si se usa Chrome (configuración por defecto), Selenium ya gestiona automaticamente el `chromedriver`.

---

## Como Ejecutar las Pruebas

Todos los tests se ejecutan utilizando el runner Pytest desde la raiz del proyecto.


### Ejecucion Completa (UI y API)

Ejecuta todos los tests y genera el reporte HTML:
`pytest --html=reports/report_all.html --self-contained-html`

### Ejecucion por Categoria (Tags)

Se pueden usar los marks (`@pytest.mark.ui` o `@pytest.mark.api`) definidos en los tests:
**Solo pruebas UI (Selenium):** 
 `pytest -m ui` 
**Solo pruebas API (REST)** 
 `pytest -m api` 

### Modo Headless (Sin abrir ventana del navegador)

Para las pruebas UI, puedes ejecutarlas en modo sin cabeza (más rápido para CI/CD):
`pytest -m ui --run-headless`

## Como Interpretar los Reportes Generados

Despues de ejecutar los tests, se generan archivos de salida en el directorio `reports/`.

### Reporte HTML (`report_all.html`):

- **Acceso:** Abre el archivo `reports/report_all.html` en cualquier navegador web.
- **Contenido:** Proporciona un resumen de la ejecución (Total Passed/Failed), la duración y una tabla detallada de cada caso de prueba.
- **Filtros:** Permite filtrar fácilmente por estado (`Passed`, `Failed`).
- **Screenshots:** En caso de que un test UI falle, la captura de pantalla del error se adjunta directamente al reporte, bajo la sección del test fallido.

### Logs (`automation_events.log`):

- **Acceso:** El archivo se encuentra en `reports/automation_events.log`.
- **Contenido:** Contiene un registro secuencial de todos los eventos críticos del *framework*, incluyendo la inicialización de *drivers*, la creación de *API Clients* y cualquier mensaje de error o fallo capturado por el *logger*.

### Capturas de Pantalla:

- **Ubicacion:** Se guardan en `reports/screenshots/`.
- **Nomenclatura:** Los archivos tienen el formato `FAIL_<nombre_del_test>_<timestamp>.png` y solo se generan cuando un test UI falla.