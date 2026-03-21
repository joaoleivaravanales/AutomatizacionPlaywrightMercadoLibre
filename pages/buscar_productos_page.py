from playwright.sync_api import Page, expect

class BuscarPage:

    def __init__(self, page: Page):
        self.page = page

        # LOCATORS (preferir role/label)
        self.input_busqueda = page.get_by_placeholder("Buscar productos, marcas y más")
        self.btn_buscar = page.get_by_role("button", name="Buscar")
        self.resultados = self.page.locator(".ui-search-layout__item")
        self.primer_resultado = page.locator(".ui-search-result__content").first

    def open_home(self, base_url):
        self.page.goto(base_url)

    def buscar_producto(self, producto: str):
        self.input_busqueda.fill(producto)
        self.input_busqueda.press("Enter")

    def validar_resultados(self):
            expect(self.resultados.first).to_be_visible(timeout=10000)

    def seleccionar_primer_producto(self):
        self.primer_resultado.click()