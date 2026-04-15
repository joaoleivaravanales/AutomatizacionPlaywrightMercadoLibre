from pytest_bdd import scenario, given, when, parsers
import pytest
from pages.validar_textos_iphone import ValidarTextosIphonePage

@scenario('../features/validar_iphone.feature', 'Validar textos do iPhone')
def test_validar_textos_iphone():    pass

@pytest.fixture
def validar_textos_iphone_page(page):
    return ValidarTextosIphonePage(page)

@given('el usuario está en la pagina principal')
def abrir_pagina_principal(validar_textos_iphone_page):
    validar_textos_iphone_page.abrir_pagina_principal()

@when(parsers.parse('busca el producto "{producto}"'))
def buscar_producto(validar_textos_iphone_page, producto):
    validar_textos_iphone_page.buscar_producto(producto)

@when('selecciono el segundo resultado del producto')
def seleccionar_segundo_resultado(validar_textos_iphone_page):
    validar_textos_iphone_page.seleccionar_segundo_resultado()
