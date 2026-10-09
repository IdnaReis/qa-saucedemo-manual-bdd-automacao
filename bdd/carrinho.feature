# language: pt
Funcionalidade: Carrinho de compras
  Como cliente logado
  Quero gerenciar os itens do carrinho
  Para comprar apenas o que desejo

  Contexto:
    Dado que estou logado com "standard_user"

  Cenário: CT09 - Adicionar produto ao carrinho
    Quando adiciono um produto ao carrinho
    Então o ícone do carrinho deve mostrar "1"
    E o botão do produto deve mudar para "Remove"

  Cenário: CT10 - Remover produto do carrinho
    Dado que tenho 1 produto no carrinho
    Quando removo o produto na tela do carrinho
    Então o carrinho deve ficar vazio

  Cenário: CT11 - Carrinho mantém itens ao navegar
    Dado que tenho 2 produtos no carrinho
    Quando volto para a lista de produtos e abro o carrinho novamente
    Então os 2 produtos devem continuar no carrinho
