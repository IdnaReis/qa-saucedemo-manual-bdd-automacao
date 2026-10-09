class CartPage:
    def __init__(self, page):
        self.page = page
        self.lista = page.locator(".cart_list")
        self.itens = page.locator(".cart_item")
        self.nomes = page.locator(".cart_item .inventory_item_name")
        self.precos = page.locator(".cart_item .inventory_item_price")
        self.botao_checkout = page.locator("#checkout")
        self.continuar_comprando = page.locator("#continue-shopping")

    def remover_primeiro(self):
        self.itens.first.get_by_role("button", name="Remove").click()

    def checkout(self):
        self.botao_checkout.click()
