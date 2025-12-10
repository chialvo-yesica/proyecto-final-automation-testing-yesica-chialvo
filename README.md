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