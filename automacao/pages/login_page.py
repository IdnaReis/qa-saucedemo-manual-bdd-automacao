class LoginPage:
    """Tela de login do SauceDemo."""

    def __init__(self, page):
        self.page = page
        self.usuario = page.locator("#user-name")
        self.senha = page.locator("#password")
        self.botao_login = page.locator("#login-button")
        self.erro = page.locator("[data-test='error']")

    def abrir(self):
        self.page.goto("/")

    def preencher(self, usuario, senha):
        self.usuario.fill(usuario)
        self.senha.fill(senha)

    def entrar(self):
        self.botao_login.click()

    def login(self, usuario, senha):
        self.abrir()
        self.preencher(usuario, senha)
        self.entrar()
