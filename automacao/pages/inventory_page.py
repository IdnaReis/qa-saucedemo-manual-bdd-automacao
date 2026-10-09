class InventoryPage:
    """Lista de produtos, detalhes do produto e menu."""

    def __init__(self, page):
        self.page = page
        self.titulo = page.locator(".title")
        self.itens = page.locator(".inventory_item")
        self.nomes = page.locator(".inventory_item_name")
        self.precos = page.locator(".inventory_item_price")
        self.ordenacao = page.locator(".product_sort_container")
        self.badge_carrinho = page.locator(".shopping_cart_badge")
        self.link_carrinho = page.locator(".shopping_cart_link")

    def item(self, nome):
        return self.itens.filter(has_text=nome)

    def botao(self, nome):
        return self.item(nome).locator("button")

    def adicionar(self, nome):
        self.item(nome).get_by_role("button", name="Add to cart").click()

    def imagem(self, nome):
        return self.item(nome).locator("img.inventory_item_img")

    def lista_nomes(self):
        return self.nomes.all_inner_texts()

    def lista_precos(self):
        return [float(p.replace("$", "")) for p in self.precos.all_inner_texts()]

    def ordenar(self, opcao):
        self.ordenacao.select_option(label=opcao)

    def abrir_carrinho(self):
        self.link_carrinho.click()

    def logout(self):
        self.page.locator("#react-burger-menu-btn").click()
        self.page.locator("#logout_sidebar_link").click()


class ProductDetailsPage:
    def __init__(self, page):
        self.nome = page.locator(".inventory_details_name")
        self.descricao = page.locator(".inventory_details_desc")
        self.preco = page.locator(".inventory_details_price")
        self.imagem = page.locator("img.inventory_details_img")
        self.voltar = page.locator("#back-to-products")
