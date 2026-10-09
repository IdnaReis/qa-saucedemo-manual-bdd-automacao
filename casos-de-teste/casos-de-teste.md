# 🧪 Casos de Teste — SauceDemo

Pré-condição geral: acessar https://www.saucedemo.com. Senha: `secret_sauce`.

## 🔐 Login

### CT01 — Login com credenciais válidas
| Campo | Descrição |
|---|---|
| Prioridade | Alta |
| Pré-condição | Estar na tela de login |
| Passos | 1. Informar usuário `standard_user` 2. Informar senha `secret_sauce` 3. Clicar em **Login** |
| Resultado esperado | Usuário é direcionado para a página de produtos (título "Products") |

### CT02 — Login com senha inválida
| Campo | Descrição |
|---|---|
| Prioridade | Alta |
| Pré-condição | Estar na tela de login |
| Passos | 1. Informar usuário `standard_user` 2. Informar senha `senha_errada` 3. Clicar em **Login** |
| Resultado esperado | Mensagem: "Epic sadface: Username and password do not match any user in this service". Usuário permanece na tela de login |

### CT03 — Login com usuário bloqueado
| Campo | Descrição |
|---|---|
| Prioridade | Alta |
| Pré-condição | Estar na tela de login |
| Passos | 1. Informar usuário `locked_out_user` 2. Informar senha `secret_sauce` 3. Clicar em **Login** |
| Resultado esperado | Mensagem: "Epic sadface: Sorry, this user has been locked out." Acesso negado |

### CT04 — Login com campos vazios
| Campo | Descrição |
|---|---|
| Prioridade | Média |
| Pré-condição | Estar na tela de login |
| Passos | 1. Deixar usuário e senha em branco 2. Clicar em **Login** |
| Resultado esperado | Mensagem: "Epic sadface: Username is required" |

## 🛍️ Catálogo

### CT05 — Exibição da lista de produtos
| Campo | Descrição |
|---|---|
| Prioridade | Alta |
| Pré-condição | Logado com `standard_user` |
| Passos | 1. Observar a página de produtos |
| Resultado esperado | 6 produtos exibidos, cada um com imagem, nome, descrição, preço e botão **Add to cart** |

### CT06 — Ordenar por preço (menor para maior)
| Campo | Descrição |
|---|---|
| Prioridade | Média |
| Pré-condição | Logado com `standard_user` |
| Passos | 1. No filtro, selecionar **Price (low to high)** |
| Resultado esperado | Produtos ordenados do menor para o maior preço |

### CT07 — Ordenar por nome (Z a A)
| Campo | Descrição |
|---|---|
| Prioridade | Baixa |
| Pré-condição | Logado com `standard_user` |
| Passos | 1. No filtro, selecionar **Name (Z to A)** |
| Resultado esperado | Produtos em ordem alfabética inversa |

### CT08 — Visualizar detalhes do produto
| Campo | Descrição |
|---|---|
| Prioridade | Média |
| Pré-condição | Logado com `standard_user` |
| Passos | 1. Clicar no nome de um produto |
| Resultado esperado | Página de detalhes com nome, descrição, preço e imagem iguais aos da listagem, e botão **Back to products** |

## 🛒 Carrinho

### CT09 — Adicionar produto ao carrinho
| Campo | Descrição |
|---|---|
| Prioridade | Alta |
| Pré-condição | Logado com `standard_user`, carrinho vazio |
| Passos | 1. Clicar em **Add to cart** em um produto |
| Resultado esperado | Ícone do carrinho mostra "1" e o botão muda para **Remove** |

### CT10 — Remover produto do carrinho
| Campo | Descrição |
|---|---|
| Prioridade | Alta |
| Pré-condição | 1 produto no carrinho |
| Passos | 1. Abrir o carrinho 2. Clicar em **Remove** |
| Resultado esperado | Produto sai da lista e o número no ícone do carrinho desaparece |

### CT11 — Carrinho mantém itens ao navegar
| Campo | Descrição |
|---|---|
| Prioridade | Média |
| Pré-condição | 2 produtos no carrinho |
| Passos | 1. Abrir o carrinho 2. Clicar em **Continue Shopping** 3. Abrir o carrinho novamente |
| Resultado esperado | Os 2 produtos continuam no carrinho |

## 💳 Checkout

### CT12 — Compra completa com sucesso
| Campo | Descrição |
|---|---|
| Prioridade | Alta |
| Pré-condição | 1 produto no carrinho |
| Passos | 1. Abrir o carrinho 2. **Checkout** 3. Preencher Nome, Sobrenome e CEP 4. **Continue** 5. **Finish** |
| Resultado esperado | Mensagem "Thank you for your order!" exibida |

### CT13 — Checkout sem o nome
| Campo | Descrição |
|---|---|
| Prioridade | Alta |
| Pré-condição | 1 produto no carrinho, na tela de dados do checkout |
| Passos | 1. Deixar **First Name** vazio 2. Preencher Sobrenome e CEP 3. **Continue** |
| Resultado esperado | Mensagem "Error: First Name is required". Não avança |

### CT14 — Checkout sem o CEP
| Campo | Descrição |
|---|---|
| Prioridade | Alta |
| Pré-condição | 1 produto no carrinho, na tela de dados do checkout |
| Passos | 1. Preencher Nome e Sobrenome 2. Deixar **Postal Code** vazio 3. **Continue** |
| Resultado esperado | Mensagem "Error: Postal Code is required". Não avança |

### CT15 — Cálculo do valor total
| Campo | Descrição |
|---|---|
| Prioridade | Alta |
| Pré-condição | 2 produtos no carrinho, na tela de resumo (Checkout: Overview) |
| Passos | 1. Somar os preços dos itens 2. Comparar com **Item total** 3. Conferir se **Total** = Item total + Tax |
| Resultado esperado | Item total igual à soma dos itens e Total igual a Item total + Tax |
