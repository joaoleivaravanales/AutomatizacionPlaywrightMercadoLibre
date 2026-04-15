from playwright.sync_api import Page

class ValidarTextosIphonePage:

    def __init__(self, page: Page):
        self.page = page
        # LOCATORS
        self.txt_busqueda = page.get_by_placeholder("Buscar productos, marcas y más")
        self.resultados_busqueda = page.locator(".ui-search-layout__item")

    def abrir_pagina_principal(self):
        self.page.goto("https://www.mercadolibre.com", wait_until="domcontentloaded")

    def buscar_producto(self, producto):
        self.txt_busqueda.click()
        self.txt_busqueda.fill(producto)
        self.txt_busqueda.press("Enter")

    def seleccionar_segundo_resultado(self):
        productos = self.resultados_busqueda
        self.page.wait_for_selector(".ui-search-layout__item", timeout=10000)
        assert productos.count() > 1, "No hay suficientes resultados"
        producto = productos.nth(1)
        link = producto.locator("a").first
        link.scroll_into_view_if_needed()
        link.click()
        self.page.wait_for_load_state("domcontentloaded")