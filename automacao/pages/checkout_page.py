def _valor(texto):
    return float(texto.split("$")[1])


class CheckoutPage:
    """Dados do comprador, resumo do pedido e confirmação."""

    def __init__(self, page):
        self.page = page
        self.nome = page.locator("#first-name")
        self.sobrenome = page.locator("#last-name")
        self.cep = page.locator("#postal-code")
        self.botao_continuar = page.locator("#continue")
        self.botao_finalizar = page.locator("#finish")
        self.erro = page.locator("[data-test='error']")
        self.precos_itens = page.locator(".cart_item .inventory_item_price")
        self.item_total = page.locator(".summary_subtotal_label")
        self.taxa = page.locator(".summary_tax_label")
        self.total = page.locator(".summary_total_label")
        self.confirmacao = page.locator(".complete-header")

    def preencher(self, nome="Ana", sobrenome="Silva", cep="72870000"):
        if nome:
            self.nome.fill(nome)
        if sobrenome:
            self.sobrenome.fill(sobrenome)
        if cep:
            self.cep.fill(cep)

    def continuar(self):
        self.botao_continuar.click()

    def finalizar(self):
        self.botao_finalizar.click()

    def valor_item_total(self):
        return _valor(self.item_total.inner_text())

    def valor_taxa(self):
        return _valor(self.taxa.inner_text())

    def valor_total(self):
        return _valor(self.total.inner_text())

    def soma_itens(self):
        return round(sum(_valor(p) for p in self.precos_itens.all_inner_texts()), 2)
