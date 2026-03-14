from playwright.sync_api import Page

class RegistrarPage:

    def __init__(self, page: Page):
        self.page = page

        # LOCATORS
        self.btn_crear_cuenta = page.get_by_role("link", name="Crea tu cuenta")
        self.txt_email = page.get_by_test_id("email")
        self.txt_telefono = page.get_by_test_id("phone")
        self.txt_nombre_completo = page.get_by_test_id("first_name")
        self.txt_contrasena = page.get_by_test_id("password")
        self.btn_continuar = page.get_by_test_id("submit")
        

    def open(self, base_url):
        self.page.goto(base_url)

    def click_crear_cuenta(self):
        self.btn_crear_cuenta.click()
    
    def click_continuarCrear(self):
        self.btn_continuar.click()

    def ingresar_datos_formularios(self, campo, valor):
        match campo:
            case "email":
                self.txt_email.click()
                self.txt_email.fill(valor)
            case "telefono":
                self.txt_telefono.click()
                self.txt_telefono.fill(valor)
            case "nombreCompleto":    
                self.txt_nombre_completo.click()
                self.txt_nombre_completo.fill(valor)
            case "contrasena":
                self.txt_contrasena.click()
                self.txt_contrasena.fill(valor)    
                