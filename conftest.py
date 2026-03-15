import pytest
from playwright.sync_api import sync_playwright
import os
from datetime import datetime
from utils.reporte_pdf import generar_reporte_pdf
from utils.screenshot import screenshots_steps


@pytest.fixture(scope="session")
def base_url():
    return "https://www.mercadolibre.cl"


@pytest.fixture
def page():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    yield page

    input("Presiona ENTER para cerrar el navegador...")
    browser.close()
    p.stop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":

        resultado = "PASSED"

        if rep.failed:
            resultado = "FAILED"

        print("Generando PDF con screenshots:", screenshots_steps)

        generar_reporte_pdf(
            nombre_test=item.originalname,
            resultado=resultado,
            screenshots=screenshots_steps
        )

        screenshots_steps.clear()