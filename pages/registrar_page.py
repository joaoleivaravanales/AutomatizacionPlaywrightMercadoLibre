from playwright.sync_api import Page

class RegistrarPage:

    def __init__(self, page: Page):
        self.page = page
        # LOCATORS
        self.btn_crear_cuenta = page.locator('[data-link-id="registration"]')
      #  self.txt_email = page.get_by_test_id("email")
        self.txt_email = self.page.locator('input[data-testid="email"]')
        self.txt_telefono = self.page.locator('input[data-testid="phone"]')
        self.txt_nombre_completo = self.page.locator('input[data-testid="first_name"]')
        self.txt_contrasena = self.page.locator('input[data-testid="password"]')
        self.btn_continuar = self.page.locator('button[data-testid="submit"]')
        

    def open(self, base_url):
        self.page.goto(base_url)
        self.page.wait_for_load_state("domcontentloaded")

    def click_crear_cuenta(self):
        self.btn_crear_cuenta.click()
    
    def click_continuarCrear(self):
        self.btn_continuar.click()

    def ingresar_datos_formularios(self, campo, valor):
        match campo:
            case "email":
                self.page.wait_for_load_state("domcontentloaded")
                self.txt_email.wait_for(state="visible", timeout=5000)
                self.txt_email.click()
                self.txt_email.fill(valor)
            case "telefono":
                self.txt_telefono.wait_for(state="visible", timeout=5000)
                self.txt_telefono.click()
                self.txt_telefono.fill(valor)
            case "nombreCompleto":    
                self.txt_nombre_completo.wait_for(state="visible", timeout=5000)
                self.txt_nombre_completo.click()
                self.txt_nombre_completo.fill(valor)
            case "contrasena":
                self.txt_contrasena.wait_for(state="visible", timeout=5000)
                self.txt_contrasena.click()
                self.txt_contrasena.fill(valor)    
                