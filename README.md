# Pre-entrega Automation Testing- Ivana Papaño

Proyecto de automatización para el sitio SauceDemo - Talento Tech 2026


## Temario
* [1. Propósito del Proyecto](#1-propósito-del-proyecto)
* [2. Tecnologías Utilizadas](#2-tecnologías-utilizadas)
* [3. Estructura de Carpetas](#3-estructura-de-carpetas)
* [4. Casos de Prueba Automatizados](#4-casos-de-prueba-automatizados)
* [5. Instrucciones de Ejecución](#5-instrucciones-de-ejecución)
* [6. Evidencias](#6-evidencias)

---

## 1. Propósito del Proyecto
Este proyecto desarrolla la automatización de pruebas para el sitio **SauceDemo**. Se enfoca en validar el flujo de autenticación (Login) y la salida del sistema (Logout), asegurando que la navegación hacia el inventario sea correcta y estable mediante el uso de esperas explícitas.

## 2. Tecnologías Utilizadas
* **Lenguaje:** Python 3.13
* **Framework de Pruebas:** Pytest
* **Herramienta de Automatización:** Selenium WebDriver
* **Patrón de Diseño:** Page Object Model (POM)
* **Reportes:** Pytest-html

## 3. Estructura de Carpetas
Siguiendo los lineamientos de la pre-entrega, el proyecto se organiza de la siguiente manera:
* `Tests/`: Scripts de prueba independientes para cada caso de uso.
* `Utils/`: Lógica de soporte y Page Objects (`LoginPage.py`).
* `Reports/`: Almacena el reporte final HTML y las capturas de pantalla de evidencia.
* `datos/`: Carpeta destinada a futuros archivos de datos externos (CSV/JSON).

## 4. Casos de Prueba Automatizados
Se implementaron validaciones con **WebDriverWait** para asegurar la estabilidad:
* **Login Exitoso**: Validación de redirección a `/inventory.html`.
* **Login Fallido**: Validación de mensaje de error por credenciales incorrectas.
* **Login Bloqueado**: Validación de mensaje de alerta para usuario `locked_out_user`.
* **Logout**: Verificación de retorno exitoso al formulario de inicio.

## 5. Instrucciones de Ejecución

Para ejecutar las pruebas y generar el reporte técnico, utilice el siguiente comando en la terminal:

```bash
py -m pytest Tests/ -v --html=Reports/reporte_final.html



## 6. Evidencias

Los resultados de la última ejecución muestran un **100% de éxito (4/4 tests passed)**. 

Puede encontrar el reporte detallado en `Reports/reporte_final.html` y las capturas de pantalla en `Reports/capturasPantalla/`.
