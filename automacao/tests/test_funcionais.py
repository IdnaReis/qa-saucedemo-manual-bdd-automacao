"""Executa os 15 cenários documentados nos testes manuais (pasta bdd/)."""
from pytest_bdd import scenarios

scenarios(
    "login.feature",
    "catalogo.feature",
    "carrinho.feature",
    "checkout.feature",
)
