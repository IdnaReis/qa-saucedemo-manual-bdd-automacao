"""Step definitions compartilhados pelos cenários Gherkin da pasta bdd/."""
import re

import pytest
from playwright.sync_api import expect
from pytest_bdd import given, parsers, then, when

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage, ProductDetailsPage
from pages.login_page import LoginPage

SENHA = "secret_sauce"
BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"


# ---------------------------------------------------------------------------
# Bugs conhecidos: cenários com tag @BUG-xxx viram "falha esperada" (xfail)
# ---------------------------------------------------------------------------
def pytest_bdd_apply_tag(tag, function):
    if tag.startswith("BUG-"):
        motivo = f"{tag}: bug conhecido (ver pasta bugs/)"
        pytest.mark.xfail(reason=motivo, strict=False)(function)
        return True
    return None


@pytest.fixture
def ctx():
    """Guarda informações entre os passos de um mesmo cenário."""
    return {}


@pytest.fixture
def inventory(page):
    return InventoryPage(page)


@pytest.fixture
def cart(page):
    return CartPage(page)


@pytest.fixture
def checkout(page):
    return CheckoutPage(page)


def ir_para_resumo(inventory, cart, checkout):
    inventory.abrir_carrinho()
    cart.checkout()
    checkout.preencher()
    checkout.continuar()


# ---------------------------------------------------------------------------
# Login
# ---------------------------------------------------------------------------
@given("que estou na tela de login do SauceDemo")
def tela_login(page):
    LoginPage(page).abrir()


@given(parsers.parse('que estou logado com "{usuario}"'))
def logado(page, usuario):
    LoginPage(page).login(usuario, SENHA)
    expect(page).to_have_url(re.compile("inventory"))


@when(parsers.parse('informo o usuário "{usuario}" e a senha "{senha}"'))
def informa_credenciais(page, usuario, senha):
    LoginPage(page).preencher(usuario, senha)


@when("clico em Login")
def clica_login(page):
    LoginPage(page).entrar()


@when("clico em Login sem preencher os campos")
def clica_login_vazio(page):
    LoginPage(page).entrar()


@then("devo ver a página de produtos")
def pagina_produtos(page, inventory):
    expect(page).to_have_url(re.compile("inventory"))
    expect(inventory.titulo).to_have_text("Products")


@then(parsers.parse('devo ver a mensagem "{mensagem}"'))
def ve_mensagem(page, mensagem):
    expect(page.locator("body")).to_contain_text(mensagem)


# ---------------------------------------------------------------------------
# Catálogo
# ---------------------------------------------------------------------------
@then('devo ver 6 produtos com imagem, nome, descrição, preço e botão "Add to cart"')
def seis_produtos(inventory):
    expect(inventory.itens).to_have_count(6)
    for i in range(6):
        item = inventory.itens.nth(i)
        expect(item.locator("img.inventory_item_img")).to_be_visible()
        expect(item.locator(".inventory_item_name")).not_to_be_empty()
        expect(item.locator(".inventory_item_desc")).not_to_be_empty()
        expect(item.locator(".inventory_item_price")).to_contain_text("$")
        expect(item.locator("button")).to_have_text("Add to cart")


@when(parsers.parse('seleciono a ordenação "{opcao}"'))
def ordena(inventory, opcao):
    inventory.ordenar(opcao)


@then("os produtos devem aparecer do menor para o maior preço")
def ordem_preco(inventory):
    precos = inventory.lista_precos()
    assert precos == sorted(precos), precos


@then("os produtos devem aparecer em ordem alfabética inversa")
def ordem_z_a(inventory):
    nomes = inventory.lista_nomes()
    assert nomes == sorted(nomes, reverse=True), nomes


@when("clico no nome de um produto")
def clica_produto(inventory, ctx):
    item = inventory.item(BACKPACK)
    ctx["listagem"] = {
        "nome": item.locator(".inventory_item_name").inner_text(),
        "descricao": item.locator(".inventory_item_desc").inner_text(),
        "preco": item.locator(".inventory_item_price").inner_text(),
        "imagem": inventory.imagem(BACKPACK).get_attribute("src"),
    }
    item.locator(".inventory_item_name").click()


@then("devo ver os mesmos nome, descrição, preço e imagem da listagem")
def detalhes_iguais(page, ctx):
    detalhe = ProductDetailsPage(page)
    esperado = ctx["listagem"]
    expect(detalhe.nome).to_have_text(esperado["nome"])
    expect(detalhe.descricao).to_have_text(esperado["descricao"])
    expect(detalhe.preco).to_have_text(esperado["preco"])
    expect(detalhe.imagem).to_have_attribute("src", esperado["imagem"])
    expect(detalhe.voltar).to_be_visible()


# ---------------------------------------------------------------------------
# Carrinho
# ---------------------------------------------------------------------------
@when("adiciono um produto ao carrinho")
def adiciona_um(inventory, ctx):
    inventory.adicionar(BACKPACK)
    ctx["produto"] = BACKPACK


@when(parsers.parse('adiciono "{produto}" ao carrinho'))
def adiciona_produto(inventory, ctx, produto):
    inventory.adicionar(produto)
    ctx["produto"] = produto


@then(parsers.parse('o ícone do carrinho deve mostrar "{quantidade}"'))
def badge(inventory, quantidade):
    expect(inventory.badge_carrinho).to_have_text(quantidade)


@then(parsers.parse('o botão do produto deve mudar para "{texto}"'))
def botao_muda(inventory, ctx, texto):
    expect(inventory.botao(ctx["produto"])).to_have_text(texto)


@given("que tenho 1 produto no carrinho")
def um_produto(inventory):
    inventory.adicionar(BACKPACK)


@given("que tenho 2 produtos no carrinho")
def dois_produtos(inventory):
    inventory.adicionar(BACKPACK)
    inventory.adicionar(BIKE_LIGHT)


@when("removo o produto na tela do carrinho")
def remove_no_carrinho(inventory, cart):
    inventory.abrir_carrinho()
    cart.remover_primeiro()


@then("o carrinho deve ficar vazio")
def carrinho_vazio(inventory, cart):
    expect(cart.itens).to_have_count(0)
    expect(inventory.badge_carrinho).to_have_count(0)


@when("volto para a lista de produtos e abro o carrinho novamente")
def navega_e_volta(inventory, cart):
    inventory.abrir_carrinho()
    cart.continuar_comprando.click()
    inventory.abrir_carrinho()


@then("os 2 produtos devem continuar no carrinho")
def dois_no_carrinho(cart):
    expect(cart.nomes).to_have_text([BACKPACK, BIKE_LIGHT])


# ---------------------------------------------------------------------------
# Checkout
# ---------------------------------------------------------------------------
@given("tenho produtos no carrinho")
def tem_produtos(inventory):
    inventory.adicionar(BACKPACK)
    inventory.adicionar(BIKE_LIGHT)


@when("preencho nome, sobrenome e CEP e finalizo a compra")
def compra_completa(inventory, cart, checkout):
    ir_para_resumo(inventory, cart, checkout)
    checkout.finalizar()


@when("deixo o nome vazio e clico em Continue")
def sem_nome(inventory, cart, checkout):
    inventory.abrir_carrinho()
    cart.checkout()
    checkout.preencher(nome=None)
    checkout.continuar()


@when("deixo o CEP vazio e clico em Continue")
def sem_cep(inventory, cart, checkout):
    inventory.abrir_carrinho()
    cart.checkout()
    checkout.preencher(cep=None)
    checkout.continuar()


@when("chego na tela de resumo do pedido")
def chega_resumo(inventory, cart, checkout):
    ir_para_resumo(inventory, cart, checkout)


@given("estou na tela de resumo do pedido")
def esta_no_resumo(inventory, cart, checkout):
    ir_para_resumo(inventory, cart, checkout)


@then("o Item total deve ser a soma dos preços dos itens")
def item_total_soma(checkout):
    assert checkout.valor_item_total() == checkout.soma_itens()


@then("o Total deve ser o Item total mais a taxa")
def total_com_taxa(checkout):
    esperado = round(checkout.valor_item_total() + checkout.valor_taxa(), 2)
    assert checkout.valor_total() == esperado


# ---------------------------------------------------------------------------
# Regressão dos bugs (bdd/bugs-encontrados.feature)
# ---------------------------------------------------------------------------
@given("meu carrinho está vazio")
def garante_carrinho_vazio(inventory):
    expect(inventory.badge_carrinho).to_have_count(0)


@when("clico em Checkout")
def clica_checkout(inventory, cart):
    inventory.abrir_carrinho()
    cart.checkout()


@then("devo ver uma mensagem informando que o carrinho está vazio")
def mensagem_carrinho_vazio(page):
    expect(page.locator("body")).to_contain_text(re.compile("empty|vazio", re.I))


@then("não devo avançar para a tela de dados do comprador")
def nao_avanca(page):
    expect(page).not_to_have_url(re.compile("checkout-step-one"))


@then(parsers.parse('o Item total deve ser exibido como "{valor}"'))
def item_total_formatado(checkout, valor):
    expect(checkout.item_total).to_have_text(f"Item total: {valor}")


@when("observo a página de produtos")
def observa_produtos(inventory):
    expect(inventory.itens).to_have_count(6)


@then("cada produto deve exibir uma imagem diferente")
def imagens_diferentes(inventory):
    imagens = [
        inventory.itens.nth(i).locator("img.inventory_item_img").get_attribute("src")
        for i in range(6)
    ]
    assert len(set(imagens)) == 6, imagens


@then(parsers.parse('o primeiro produto deve ser "{nome}"'))
def primeiro_produto(inventory, nome):
    expect(inventory.nomes.first).to_have_text(nome)


@when(parsers.parse('clico no nome "{nome}"'))
def clica_nome(inventory, nome):
    inventory.item(nome).locator(".inventory_item_name").click()


@then(parsers.parse('devo ver a página da "{nome}" com preço "{preco}"'))
def pagina_produto(page, nome, preco):
    detalhe = ProductDetailsPage(page)
    expect(detalhe.nome).to_have_text(nome)
    expect(detalhe.preco).to_have_text(preco)


@when(parsers.parse('preencho o Last Name com "{texto}"'))
def preenche_sobrenome(inventory, cart, checkout, texto):
    inventory.abrir_carrinho()
    cart.checkout()
    checkout.nome.fill("Ana")
    checkout.sobrenome.fill(texto)


@then(parsers.parse('o campo Last Name deve exibir "{texto}"'))
def sobrenome_exibido(checkout, texto):
    expect(checkout.sobrenome).to_have_value(texto)


@then(parsers.parse('se o Last Name ficar vazio devo ver "{mensagem}"'))
def sobrenome_obrigatorio(checkout, mensagem):
    checkout.sobrenome.fill("")
    checkout.cep.fill("72870000")
    checkout.continuar()
    expect(checkout.erro).to_have_text(mensagem)


@when("clico em Finish")
def clica_finish(checkout):
    checkout.finalizar()


@given(parsers.parse('que o "{usuario}" deixou um produto no carrinho e fez logout'))
def outro_usuario_deixou_produto(page, inventory, usuario):
    LoginPage(page).login(usuario, SENHA)
    inventory.adicionar(BACKPACK)
    inventory.logout()


@when(parsers.parse('faço login com "{usuario}"'))
def faz_login(page, usuario):
    login = LoginPage(page)
    login.preencher(usuario, SENHA)
    login.entrar()


@then("meu carrinho deve estar vazio")
def meu_carrinho_vazio(inventory):
    expect(inventory.badge_carrinho).to_have_count(0)


@when(parsers.parse('observo o preço da "{nome}" na listagem'))
def observa_preco(inventory, ctx, nome):
    ctx["produto"] = nome
    ctx["preco_listagem"] = inventory.item(nome).locator(".inventory_item_price").inner_text()


@then(parsers.parse('o preço deve ser "{preco}"'))
def preco_correto(ctx, preco):
    assert ctx["preco_listagem"] == preco, ctx["preco_listagem"]


@then("deve ser igual ao preço exibido no carrinho e no resumo")
def preco_consistente(inventory, cart, checkout, ctx):
    inventory.adicionar(ctx["produto"])
    inventory.abrir_carrinho()
    expect(cart.precos.first).to_have_text(ctx["preco_listagem"])
    cart.checkout()
    checkout.preencher()
    checkout.continuar()
    expect(checkout.precos_itens.first).to_have_text(ctx["preco_listagem"])


@then(parsers.parse('a imagem da "{nome}" deve ser a da mochila'))
def imagem_mochila(inventory, nome):
    expect(inventory.imagem(nome)).to_have_attribute("src", re.compile("backpack"))


@then("o ícone do carrinho deve estar no canto superior direito")
def posicao_carrinho(inventory):
    carrinho = inventory.link_carrinho.bounding_box()
    filtro = inventory.ordenacao.bounding_box()
    assert carrinho["y"] < filtro["y"], (carrinho, filtro)


@then("o botão Checkout deve estar abaixo da lista de itens no carrinho")
def posicao_checkout(inventory, cart):
    inventory.adicionar(BACKPACK)
    inventory.abrir_carrinho()
    lista = cart.lista.bounding_box()
    botao = cart.botao_checkout.bounding_box()
    assert botao["y"] >= lista["y"] + lista["height"] - 1, (lista, botao)
