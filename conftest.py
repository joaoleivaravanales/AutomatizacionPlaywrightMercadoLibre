import pytest
from playwright.sync_api import sync_playwright
import os
from utils.reporte_pdf import generar_reporte_pdf
from utils.screenshot import screenshots_steps

@pytest.fixture(scope="session")
def base_url():
    return "https://www.mercadolibre.cl"

@pytest.fixture
def page(base_url):  # 👈 IMPORTANTE

    with sync_playwright() as p:

        headless = True if os.getenv("CI") else False

        browser = p.chromium.launch(
            headless=headless,
            slow_mo=500,
            args=[
                "--disable-dev-shm-usage",
                "--no-sandbox"
            ]
        )

        context = browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36" 
        )
        page = context.new_page()

        page.goto(base_url)
        page.wait_for_load_state("networkidle")

        yield page

        browser.close()

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