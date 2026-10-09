# language: pt
Funcionalidade: Checkout
  Como cliente logado
  Quero finalizar minha compra
  Para receber os produtos

  Contexto:
    Dado que estou logado com "standard_user"
    E tenho produtos no carrinho

  Cenário: CT12 - Compra completa com sucesso
    Quando preencho nome, sobrenome e CEP e finalizo a compra
    Então devo ver a mensagem "Thank you for your order!"

  Cenário: CT13 - Checkout sem o nome
    Quando deixo o nome vazio e clico em Continue
    Então devo ver a mensagem "Error: First Name is required"

  Cenário: CT14 - Checkout sem o CEP
    Quando deixo o CEP vazio e clico em Continue
    Então devo ver a mensagem "Error: Postal Code is required"

  Cenário: CT15 - Cálculo do valor total
    Quando chego na tela de resumo do pedido
    Então o Item total deve ser a soma dos preços dos itens
    E o Total deve ser o Item total mais a taxa
