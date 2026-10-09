"""Regressão dos 14 bugs encontrados nos testes exploratórios.

Cada cenário descreve o comportamento CORRETO e está marcado como
xfail (falha esperada) enquanto o bug existir. Se um bug for corrigido,
o teste aparece como XPASS no relatório.
"""
from pytest_bdd import scenarios

scenarios("bugs-encontrados.feature")
