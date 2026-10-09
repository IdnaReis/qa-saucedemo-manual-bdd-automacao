# language: pt
Funcionalidade: Regressão dos bugs encontrados nos testes exploratórios
  Cenários que descrevem o comportamento CORRETO esperado.
  Hoje falham; passarão quando os bugs forem corrigidos.

  @BUG-001
  Cenário: Bloquear checkout com carrinho vazio
    Dado que estou logado com "standard_user"
    E meu carrinho está vazio
    Quando clico em Checkout
    Então devo ver uma mensagem informando que o carrinho está vazio
    E não devo avançar para a tela de dados do comprador

  @BUG-002
  Cenário: Exibir o Item total com duas casas decimais
    Dado que estou logado com "standard_user"
    E meu carrinho está vazio
    Quando chego na tela de resumo do pedido
    Então o Item total deve ser exibido como "$0.00"

  @BUG-003
  Cenário: Cada produto exibe a própria imagem na listagem
    Dado que estou logado com "problem_user"
    Quando observo a página de produtos
    Então cada produto deve exibir uma imagem diferente

  @BUG-004
  Esquema do Cenário: Ordenar produtos
    Dado que estou logado com "problem_user"
    Quando seleciono a ordenação "<opcao>"
    Então o primeiro produto deve ser "<primeiro>"

    Exemplos:
      | opcao               | primeiro                          |
      | Price (low to high) | Sauce Labs Onesie                 |
      | Name (Z to A)       | Test.allTheThings() T-Shirt (Red) |

  @BUG-005
  Cenário: Abrir os detalhes do produto clicado
    Dado que estou logado com "problem_user"
    Quando clico no nome "Sauce Labs Backpack"
    Então devo ver a página da "Sauce Labs Backpack" com preço "$29.99"

  @BUG-006
  Esquema do Cenário: Adicionar qualquer produto ao carrinho
    Dado que estou logado com "error_user"
    Quando adiciono "<produto>" ao carrinho
    Então o botão do produto deve mudar para "Remove"

    Exemplos:
      | produto                           |
      | Sauce Labs Bolt T-Shirt           |
      | Sauce Labs Fleece Jacket          |
      | Test.allTheThings() T-Shirt (Red) |

  @BUG-007 @BUG-008
  Cenário: Exigir e aceitar o sobrenome no checkout
    Dado que estou logado com "error_user"
    E tenho produtos no carrinho
    Quando preencho o Last Name com "Silva"
    Então o campo Last Name deve exibir "Silva"
    E se o Last Name ficar vazio devo ver "Error: Last Name is required"

  @BUG-009
  Cenário: Concluir a compra
    Dado que estou logado com "error_user"
    E estou na tela de resumo do pedido
    Quando clico em Finish
    Então devo ver a mensagem "Thank you for your order!"

  @BUG-010
  Cenário: Carrinho não é compartilhado entre usuários
    Dado que o "error_user" deixou um produto no carrinho e fez logout
    Quando faço login com "performance_glitch_user"
    Então meu carrinho deve estar vazio

  @BUG-011
  Cenário: Preço da listagem igual ao preço cobrado
    Dado que estou logado com "visual_user"
    Quando observo o preço da "Sauce Labs Backpack" na listagem
    Então o preço deve ser "$29.99"
    E deve ser igual ao preço exibido no carrinho e no resumo

  @BUG-012 @BUG-013 @BUG-014
  Cenário: Layout igual ao padrão
    Dado que estou logado com "visual_user"
    Então a imagem da "Sauce Labs Backpack" deve ser a da mochila
    E o ícone do carrinho deve estar no canto superior direito
    E o botão Checkout deve estar abaixo da lista de itens no carrinho
