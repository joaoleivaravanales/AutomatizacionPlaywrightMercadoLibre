
from pytest_bdd import scenario, given, when, then, parsers
from utils.screenshot import screenshots_steps
from pages.buscar_productos_page import BuscarPage
from utils.screenshot import tomar_screenshot
from playwright.sync_api import expect
import pytest

@pytest.fixture
def buscar_page(page):
    return BuscarPage(page)

@scenario("../features/buscar_productos.feature", "Buscar productos en MercadoLibre")
def test_buscar_producto():
    pass

@given("el usuario está en la página principal")
def abrir_home(buscar_page, base_url):
    buscar_page.open_home(base_url)
    tomar_screenshot(buscar_page.page, "home_page.png")

@when(parsers.parse('busca el producto "{producto}"'))
def buscar_producto(buscar_page, producto):
    buscar_page.buscar_producto(producto)
    tomar_screenshot(buscar_page.page, "resultados_busqueda.png")

@then("debería ver resultados relacionados")
def validar_resultados(buscar_page):
    buscar_page.validar_resultados()
    tomar_screenshot(buscar_page.page, "validacion_resultados.png")