# language: pt
Funcionalidade: Catálogo de produtos
  Como cliente logado
  Quero ver e organizar os produtos
  Para encontrar o que desejo comprar

  Contexto:
    Dado que estou logado com "standard_user"

  Cenário: CT05 - Exibição da lista de produtos
    Então devo ver 6 produtos com imagem, nome, descrição, preço e botão "Add to cart"

  Cenário: CT06 - Ordenar por preço do menor para o maior
    Quando seleciono a ordenação "Price (low to high)"
    Então os produtos devem aparecer do menor para o maior preço

  Cenário: CT07 - Ordenar por nome de Z a A
    Quando seleciono a ordenação "Name (Z to A)"
    Então os produtos devem aparecer em ordem alfabética inversa

  Cenário: CT08 - Visualizar detalhes do produto
    Quando clico no nome de um produto
    Então devo ver os mesmos nome, descrição, preço e imagem da listagem
