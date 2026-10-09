# 🐞 BUG-012 — Imagem da Sauce Labs Backpack incorreta na listagem

| Campo | Descrição |
|---|---|
| **ID** | BUG-012 |
| **Módulo** | Catálogo |
| **Severidade** | Baixa |
| **Prioridade** | Média |
| **Ambiente** | Chrome 155.0.8059.40 · Windows 10 Pro 22H2 · https://www.saucedemo.com |
| **Usuário** | visual_user |
| **Caso relacionado** | Teste exploratório EXP-06 |
| **Data** | 08/10/2026 |

## Pré-condição
Usuário logado com `visual_user`.

## Passos para reproduzir
1. Observar a imagem da **Sauce Labs Backpack** na página de produtos

## Resultado esperado
Foto da mochila.

## Resultado obtido
Foto de um cachorro com uma bola na boca. Os outros 5 produtos exibem a imagem correta.

## Evidências
| Etapa | Evidência |
|---|---|
| Backpack com imagem errada | ![Backpack com imagem errada](../evidencias/exp06-1-visual-user.png) |

## Observações
Mesmo comportamento após recarregar (`exp06-2-apos-recarregar.png`).
