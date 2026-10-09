# 📊 Relatório de Execução

**Data:** 08/10/2026 · **Navegador:** Chrome 155.0.8059.40 (janela anônima) · **Sistema:** Windows 10 Pro 22H2 · **Executado por:** Idna Reis

Status: ✅ Passou · ❌ Falhou · ⛔ Bloqueado

## Casos de Teste

| ID | Caso de teste | Status | Resultado obtido | Evidência | Bug |
|---|---|---|---|---|---|
| CT01 | Login com credenciais válidas | ✅ Passou | Redirecionado para a página "Products" | [ct01](../evidencias/ct01-login-valido.png) | - |
| CT02 | Login com senha inválida | ✅ Passou | Mensagem "Epic sadface: Username and password do not match any user in this service"; campos marcados em vermelho; permaneceu no login | [ct02](../evidencias/ct02-senha-invalida.png) | - |
| CT03 | Login com usuário bloqueado | ✅ Passou | Mensagem "Epic sadface: Sorry, this user has been locked out."; acesso negado | [ct03](../evidencias/ct03-usuario-bloqueado.png) | - |
| CT04 | Login com campos vazios | ✅ Passou | Mensagem "Epic sadface: Username is required" | [ct04](../evidencias/ct04-campos-vazios.png) | - |
| CT05 | Exibição da lista de produtos | ✅ Passou | 6 produtos com imagem, nome, descrição, preço e "Add to cart". Ordenação padrão: Name (A to Z) | [ct05](../evidencias/ct05-lista-produtos.png) | - |
| CT06 | Ordenar por preço (menor → maior) | ✅ Passou | Ordem: $7.99 → $9.99 → $15.99 → $15.99 → $29.99 → $49.99 | [ct06](../evidencias/ct06-ordenar-preco.png) | - |
| CT07 | Ordenar por nome (Z → A) | ✅ Passou | Ordem: T-Shirt (Red) → Onesie → Fleece Jacket → Bolt T-Shirt → Bike Light → Backpack | [ct07](../evidencias/ct07-ordenar-nome-za.png) | - |
| CT08 | Visualizar detalhes do produto | ✅ Passou | Backpack: nome, descrição, preço ($29.99) e imagem iguais à listagem; botão "Back to products" presente e funcional | [ct08](../evidencias/ct08-detalhes-produto.png) | - |
| CT09 | Adicionar produto ao carrinho | ✅ Passou | Ícone do carrinho exibiu "1"; botão mudou para "Remove" | [ct09](../evidencias/ct09-adicionar-carrinho.png) | - |
| CT10 | Remover produto do carrinho | ✅ Passou | Produto removido da lista; contador do carrinho desapareceu | [antes](../evidencias/ct10-remover-carrinho-antes.png) · [depois](../evidencias/ct10-remover-carrinho-depois.png) | - |
| CT11 | Carrinho mantém itens ao navegar | ✅ Passou | Backpack e Bike Light permaneceram no carrinho após "Continue Shopping" | [1](../evidencias/ct11-1-carrinho-2-itens.png) · [2](../evidencias/ct11-2-carrinho-mantido.png) · [3](../evidencias/ct11-3-carrinho-mantido.png) | - |
| CT12 | Compra completa com sucesso | ✅ Passou | Mensagem "Thank you for your order!"; página checkout-complete.html; carrinho esvaziado | [ct12](../evidencias/ct12-compra-sucesso.png) | - |
| CT13 | Checkout sem o nome | ✅ Passou | Mensagem "Error: First Name is required"; não avançou | [ct13](../evidencias/ct13-checkout-sem-nome.png) | OBS-03 |
| CT14 | Checkout sem o CEP | ✅ Passou | Mensagem "Error: Postal Code is required"; não avançou | [ct14](../evidencias/ct14-checkout-sem-cep.png) | OBS-03 |
| CT15 | Cálculo do valor total | ✅ Passou | Item total $39.98 (29.99 + 9.99); Tax $3.20 (8%); Total $43.18 | [ct15](../evidencias/ct15-calculo-total.png) | - |

> Ordem de execução do checkout: CT13 → CT14 → CT15 → CT12, aproveitando os mesmos itens no carrinho.

## Resumo

| Casos executados | Passou | Falhou | Bloqueado | Exploratórios | Bugs | Observações |
|---|---|---|---|---|---|---|
| 15 | 15 | 0 | 0 | 6 sessões | 14 | 6 |

## Observações Encontradas

Comportamentos que não impediram os casos de passar, mas merecem atenção.

| ID | Descrição | Severidade sugerida | Evidência |
|---|---|---|---|
| OBS-01 | **Sessão encerrada sem aviso.** A sessão expira em cerca de 10 minutos e o usuário é deslogado sem aviso, inclusive no meio do checkout. Na primeira ocorrência, ao clicar em "Continue Shopping" o usuário foi redirecionado para o login com a mensagem "You can only access '/inventory.html' when you are logged in". Ao refazer o login, o botão funcionou normalmente, indicando expiração por tempo, e não defeito no botão. | Média | [obs-01](../evidencias/obs-sessao-encerrada.png) · [checkout](../evidencias/exp01-sessao-expirou-no-checkout.png) |
| OBS-02 | **Imagem não corresponde ao produto.** "Test.allTheThings() T-Shirt (Red)" é exibido com a foto de uma blusa de manga longa laranja, e não de uma camiseta vermelha. | Baixa | [ct05](../evidencias/ct05-lista-produtos.png) |
| OBS-03 | **Campos válidos sinalizados como erro.** No checkout, quando um campo obrigatório fica vazio, o ícone ✖ vermelho aparece em todos os campos, inclusive nos preenchidos corretamente. Confirmado em CT13 e CT14. | Baixa (usabilidade) | [ct13](../evidencias/ct13-checkout-sem-nome.png) · [ct14](../evidencias/ct14-checkout-sem-cep.png) |
| OBS-04 | **Monitoramento de erros falhando.** O Console registra requisições ao `backtrace.io` bloqueadas por CORS e respondidas com 401 e 503. Quando o BUG-009 ocorre, o envio do erro ao monitoramento também falha, ou seja, os erros não chegam à equipe. | Média | [console](../evidencias/exp04-6-console-finish.png) |
| OBS-05 | **Recibo em PDF.** Sem número do pedido; o nome do arquivo usa horário UTC (19-47) enquanto o conteúdo mostra o horário local (4:47 PM). | Baixa (melhoria) | [recibo](../evidencias/exp02-recibo-pedido-vazio.pdf) |
| OBS-06 | **performance_glitch_user.** Login, navegação para detalhes e ordenação abaixo de 2 segundos: lentidão não reproduzida nesta execução. Recomenda-se medição automatizada de tempo de resposta. | — | [print](../evidencias/exp05-2-performance-sem-lentidao.png) |

## Testes Exploratórios

| ID | Usuário | O que foi testado | O que aconteceu | Resultado |
|---|---|---|---|---|
| EXP-01 | standard_user | Checkout com carrinho vazio | Pedido sem produtos concluído (Total $0.00, "Thank you for your order!"); "Item total: $0" sem casas decimais | [BUG-001](../bugs/BUG-001-pedido-com-carrinho-vazio.md) · [BUG-002](../bugs/BUG-002-formatacao-item-total.md) |
| EXP-02 | standard_user | Botão "Generate PDF order" no pedido vazio | Recibo emitido com itens vazios e "has been dispatched" | Evidência do BUG-001 · OBS-05 |
| EXP-03 | problem_user | Imagens, adicionar/remover, ordenação, detalhes | Imagens todas iguais; adicionar/remover OK; ordenação não funciona (sem erro no Console); Backpack abre a Fleece Jacket | [BUG-003](../bugs/BUG-003-imagens-iguais-na-listagem.md) · [BUG-004](../bugs/BUG-004-ordenacao-nao-funciona.md) · [BUG-005](../bugs/BUG-005-detalhes-abrem-produto-errado.md) |
| EXP-04 | error_user | Adicionar/remover e checkout completo | Add to cart falha em 3 de 6; remover OK; Last Name não aceita texto; checkout avança sem ele; Finish dispara TypeError | [BUG-006](../bugs/BUG-006-add-to-cart-falha-em-3-produtos.md) · [BUG-007](../bugs/BUG-007-last-name-nao-aceita-digitacao.md) · [BUG-008](../bugs/BUG-008-checkout-avanca-sem-last-name.md) · [BUG-009](../bugs/BUG-009-finish-nao-conclui-compra.md) |
| EXP-05 | performance_glitch_user | Tempo de login e navegação; carrinho após troca de usuário | Tudo abaixo de 2 s; carrinho herdado do error_user | [BUG-010](../bugs/BUG-010-carrinho-compartilhado-entre-usuarios.md) · OBS-06 |
| EXP-06 | visual_user | Comparação visual com standard_user; preço cobrado no checkout | Preços aleatórios que mudam a cada carga, mas checkout cobra o real; imagem da Backpack errada; carrinho e Checkout fora do lugar | [BUG-011](../bugs/BUG-011-precos-aleatorios-na-listagem.md) · [BUG-012](../bugs/BUG-012-imagem-backpack-errada.md) · [BUG-013](../bugs/BUG-013-icone-carrinho-fora-do-lugar.md) · [BUG-014](../bugs/BUG-014-botao-checkout-fora-do-lugar.md) |

## Lições da execução

- **Confirmar o usuário antes de concluir:** a sessão expira em ~10 min; em duas ocasiões o novo login foi feito com outro usuário, o que foi identificado pela diferença visual (imagens) antes de registrar resultado.
- **Conferir a entrada de dados:** uma falha de login com `error_user` foi causada por campos trocados (senha no campo de usuário), e não por defeito.
- **Isolar no Console:** limpar o Console antes da ação para atribuir os erros à ação testada.
