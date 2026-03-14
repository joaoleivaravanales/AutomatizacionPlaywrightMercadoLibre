from pytest_bdd import scenario, given, when, then, parsers
from utils.screenshot import tomar_screenshot
from utils.screenshot import screenshots_steps
from pages.registrar_page import RegistrarPage
from playwright.sync_api import expect
import pytest

@pytest.fixture
def registrar_page(page):
    return RegistrarPage(page)

@scenario("../features/registrar_usuario.feature", "Crear nuevo usuario en mercadoLibre")
def test_registro_usuario():
    pass

@given("Visualizo al usuario que esta en la pagina")
def visualizar_usuario(registrar_page, base_url):
    registrar_page.open(base_url)
    tomar_screenshot(registrar_page.page, "pagina_registro")

@when('Presiono el boton de "Crea tu cuenta"')
def presionar_boton_crear_cuenta(registrar_page):
    registrar_page.click_crear_cuenta()
    tomar_screenshot(registrar_page.page, "crear_cuenta")

@when(parsers.parse('ingresa el dato de "{campo}" con el valor de "{valor}"'))
def step_ingresar_dato(registrar_page, campo, valor):
    registrar_page.ingresar_datos_formularios(campo, valor)
    tomar_screenshot(registrar_page.page, f"ingresar_{campo}")

@when('Presiono el boton de "Continuar"')
def step_presionar_boton(registrar_page):
    registrar_page.click_continuarCrear()
    tomar_screenshot(registrar_page.page, "continuar_crear")

@then("Visualizo el mensaje en la pantalla siguiente")
def step_validar_mensaje(registrar_page):
    expect(
        registrar_page.page.get_by_role(
            "heading",
            name="Ingresa el código que te enviamos por SMS"
        )
    ).to_be_visible()
    tomar_screenshot(registrar_page.page, "mensaje_sms")