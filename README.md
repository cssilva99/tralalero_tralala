# 📈 Personal Project

Calculadora pessoal para estimar o **valor líquido** da venda de uma posição, tendo em conta comissões, taxas de levantamento e imposto (IRS).

---

## ⚙️ Configuração

Antes de correr o programa, define as constantes no topo do ficheiro.

| Constante | Descrição |
|---|---|
| `QUANTIDADE` | Número de unidades detidas |
| `PRECO_MEDIO_EUR` | Preço médio de compra, em euros |
| `TICKER` | Símbolo do ativo (ex.: `AAPL`) |
| `PRECO_MANUAL_EUR` | Preço manual, em euros (usado quando não há cotação automática) |
| `COMISSAO_VENDA_PCT` | Comissão de venda, em percentagem |
| `COMISSAO_VENDA_MIN` | Comissão de venda mínima, em euros |
| `TAXA_LEVANTAMENTO_EUR` | Taxa de levantamento, em euros |
| `TAXA_IRS_PCT` | Taxa de IRS sobre a mais-valia, em percentagem |

### Em código

```text
const QUANTIDADE
const PRECO_MEDIO_EUR
const TICKER
const PRECO_MANUAL_EUR
const COMISSAO_VENDA_PCT
const COMISSAO_VENDA_MIN
const TAXA_LEVANTAMENTO_EUR
const TAXA_IRS_PCT
```

---

## 🧩 Funções

| Função | Descrição |
|---|---|
| `preco_atual_eur` | Obtém o preço atual do ativo, em euros |
| `calcular` | Calcula o resultado líquido da venda |
| `main` | Ponto de entrada do programa |

---

## 🚀 Utilização

1. Ajusta as constantes na secção **Configuração**.
2. Executa o programa.
3. Consulta o resultado calculado.

---

## 📝 Notas

- Os valores monetários estão todos em **euros (EUR)**.
- As percentagens (`*_PCT`) devem ser indicadas como número, por exemplo `28` para 28 %.
