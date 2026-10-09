# 📋 Plano de Testes — SauceDemo

## 1. Objetivo
Validar os fluxos principais de compra do SauceDemo (login, catálogo, carrinho e checkout) por meio de testes manuais documentados.

## 2. Ambiente
| Item | Valor |
|---|---|
| URL | https://www.saucedemo.com |
| Navegador | Google Chrome 155.0.8059.40 (64 bits) |
| Sistema | Windows 10 Pro 22H2 |
| Data da execução | 08/10/2026 |

## 3. Massa de Teste
Senha de todos os usuários: `secret_sauce`

| Usuário | Uso |
|---|---|
| `standard_user` | Fluxo principal (usuário sem problemas) |
| `locked_out_user` | Validar bloqueio de acesso |
| `problem_user` | Testes exploratórios para encontrar defeitos |
| `error_user` | Testes exploratórios para encontrar defeitos |
| `performance_glitch_user` | Testes exploratórios (lentidão) |
| `visual_user` | Testes exploratórios (falhas visuais) |

Dados de checkout: Nome `Ana`, Sobrenome `Silva`, CEP `72870000`

## 4. Escopo
**Dentro:** login, listagem e ordenação de produtos, detalhes do produto, carrinho, checkout.
**Fora:** menu lateral (About, Reset App State), testes de performance, responsividade e API.

## 5. Estratégia
- Testes funcionais manuais, positivos e negativos
- Técnicas: particionamento de equivalência e teste de campos obrigatórios
- Casos executados com `standard_user`; testes exploratórios com `problem_user` e `error_user`
- Cada caso executado gera um print em `evidencias/`

## 6. Critérios
- **Início:** site acessível e casos de teste revisados
- **Aprovado:** resultado obtido igual ao esperado
- **Reprovado:** qualquer diferença do esperado, que gera bug report
- **Fim:** 15 casos executados e todos os bugs documentados

## 7. Severidade dos Bugs
| Severidade | Quando usar |
|---|---|
| Crítica | Impede a compra ou o login |
| Alta | Funcionalidade principal com resultado errado |
| Média | Funcionalidade secundária com problema, há contorno |
| Baixa | Problema visual ou de texto |
