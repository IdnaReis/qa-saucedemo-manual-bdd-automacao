# 🧾 Testes Manuais — SauceDemo

![Testes Manuais](https://img.shields.io/badge/Testes-Manuais-6C63FF?style=for-the-badge)
![BDD](https://img.shields.io/badge/BDD%20%2F%20Gherkin-23D96C?style=for-the-badge&logo=cucumber&logoColor=white)
![Casos](https://img.shields.io/badge/Casos-15%2F15%20passaram-2EA44F?style=for-the-badge)
![Bugs](https://img.shields.io/badge/Bugs%20encontrados-14-D73A49?style=for-the-badge)

Projeto de testes manuais do e-commerce de prática [SauceDemo](https://www.saucedemo.com): planejamento, 15 casos de teste documentados, cenários em Gherkin, execução com evidências, **testes exploratórios com os 6 usuários do sistema** e **14 bugs reportados**.

## 🎯 Escopo

| Módulo | Casos | O que cobre |
|---|---|---|
| Login | 4 | Acesso válido, senha inválida, usuário bloqueado, campos vazios |
| Catálogo | 4 | Listagem, ordenação por preço e nome, detalhes do produto |
| Carrinho | 3 | Adicionar, remover, manter itens ao navegar |
| Checkout | 4 | Compra completa, campos obrigatórios, cálculo do total |
| **Total** | **15** | |

Além dos casos roteirizados, foram feitos **testes exploratórios** com `standard_user`, `problem_user`, `error_user`, `performance_glitch_user` e `visual_user`, incluindo inspeção do Console do navegador (DevTools).

## 📊 Resultado

| Casos executados | Passou | Falhou | Testes exploratórios | Bugs | Observações |
|---|---|---|---|---|---|
| 15 | 15 ✅ | 0 | 6 sessões | **14** 🐞 | 6 |

### Bugs por severidade

| Crítica | Alta | Média | Baixa |
|---|---|---|---|
| 2 | 5 | 4 | 3 |

> Detalhes em [relatório de execução](execucao/relatorio-execucao.md).

## 🐞 Bugs Encontrados

| ID | Título | Usuário | Severidade |
|---|---|---|---|
| [BUG-001](bugs/BUG-001-pedido-com-carrinho-vazio.md) | Sistema permite finalizar pedido com o carrinho vazio | standard_user | Alta |
| [BUG-002](bugs/BUG-002-formatacao-item-total.md) | "Item total" exibido sem casas decimais quando o valor é zero | standard_user | Baixa |
| [BUG-003](bugs/BUG-003-imagens-iguais-na-listagem.md) | Todos os produtos exibem a mesma imagem na listagem | problem_user | Média |
| [BUG-004](bugs/BUG-004-ordenacao-nao-funciona.md) | Ordenação de produtos não funciona e falha sem aviso | problem_user | Média |
| [BUG-005](bugs/BUG-005-detalhes-abrem-produto-errado.md) | Clicar em um produto abre a página de outro produto | problem_user | Alta |
| [BUG-006](bugs/BUG-006-add-to-cart-falha-em-3-produtos.md) | Botão Add to cart não funciona em 3 dos 6 produtos | error_user | Alta |
| [BUG-007](bugs/BUG-007-last-name-nao-aceita-digitacao.md) | Campo Last Name não aceita digitação no checkout | error_user | Alta |
| [BUG-008](bugs/BUG-008-checkout-avanca-sem-last-name.md) | Checkout avança com o campo obrigatório Last Name vazio | error_user | Média |
| [BUG-009](bugs/BUG-009-finish-nao-conclui-compra.md) | Botão Finish não conclui a compra (TypeError no clique) | error_user | **Crítica** |
| [BUG-010](bugs/BUG-010-carrinho-compartilhado-entre-usuarios.md) | Carrinho de um usuário aparece para outro no mesmo navegador | vários | Média |
| [BUG-011](bugs/BUG-011-precos-aleatorios-na-listagem.md) | Preços da listagem são aleatórios e diferentes do valor cobrado | visual_user | **Crítica** |
| [BUG-012](bugs/BUG-012-imagem-backpack-errada.md) | Imagem da Sauce Labs Backpack incorreta na listagem | visual_user | Baixa |
| [BUG-013](bugs/BUG-013-icone-carrinho-fora-do-lugar.md) | Ícone do carrinho fora da posição padrão | visual_user | Baixa |
| [BUG-014](bugs/BUG-014-botao-checkout-fora-do-lugar.md) | Botão Checkout fora da posição padrão no carrinho | visual_user | Baixa |

## 🔎 Observações

| ID | Descrição |
|---|---|
| OBS-01 | Sessão expira em ~10 min sem aviso, inclusive no meio do checkout |
| OBS-02 | Imagem da "T-Shirt (Red)" mostra uma blusa laranja de manga longa |
| OBS-03 | No checkout, campos preenchidos corretamente também recebem o ícone de erro |
| OBS-04 | Envio de erros ao serviço de monitoramento (backtrace.io) falha com CORS / 401 / 503 |
| OBS-05 | Recibo em PDF sem número do pedido; nome do arquivo em UTC e conteúdo em horário local |
| OBS-06 | `performance_glitch_user`: lentidão não reproduzida nesta execução (< 2 s) |

## 💡 Destaques

- **Causa técnica identificada:** o BUG-009 foi rastreado até um `TypeError` no `onClick` do botão Finish, via Console do DevTools
- **Impacto de negócio:** o BUG-011 mostra preços aleatórios na vitrine, mas o checkout cobra o valor real (divergência de oferta)
- **Reprodução antes de reportar:** comportamentos suspeitos foram reproduzidos e isolados (ex.: sessão expirada × defeito de botão; usuário errado × falha de ordenação)

## 📂 Estrutura

```
qa-testes-manuais-saucedemo/
├── docs/plano-de-testes.md          # Objetivo, escopo, estratégia, critérios
├── casos-de-teste/casos-de-teste.md # 15 casos com passos e resultado esperado
├── bdd/                             # Cenários Gherkin por módulo + regressão dos bugs
├── execucao/relatorio-execucao.md   # Resultado de cada caso e dos exploratórios
├── bugs/                            # 14 bug reports
└── evidencias/                      # Prints, PDF e capturas do Console
```

## 🚀 Próximos Passos

- Automatizar os cenários Gherkin com Playwright + Python (pytest-bdd)
- Transformar os bugs em testes de regressão automatizados (`bdd/bugs-encontrados.feature`)

## 👩‍💻 Autora

**Idna Reis**

QA | Analista de Qualidade | Automação de Testes

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/idna-reis)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/IdnaReis)
