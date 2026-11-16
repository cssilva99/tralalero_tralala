# 📈 Personal Project

Calculadora pessoal para estimar o **valor líquido** da venda de uma posição, tendo em conta comissões, taxas de levantamento e imposto (IRS).

---

## ⚙️ Configuration

Define const on the top of the script

| Constante | Description |
|---|---|
| `QUANTIDADE` | Número de unidades detidas |
| `PRECO_MEDIO_EUR` | Preço médio de compra, em euros |
| `TICKER` | Símbolo do ativo (ex.: `AAPL`) |
| `PRECO_MANUAL_EUR` | Preço manual, em euros (usado quando não há cotação automática) |
| `COMISSAO_VENDA_PCT` | Comissão de venda, em percentagem |
| `COMISSAO_VENDA_MIN` | Comissão de venda mínima, em euros |
| `TAXA_LEVANTAMENTO_EUR` | Taxa de levantamento, em euros |
| `TAXA_IRS_PCT` | Taxa de IRS sobre a mais-valia, em percentagem |

### const

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

| Method | Description |
|---|---|
| `preco_atual_eur` | Obtém o preço atual do ativo, em euros |
| `calcular` | Calcula o resultado líquido da venda |
| `main` | Ponto de entrada do programa |

---

## 🚀 Usage

1. Ajustes const in the **Configuration** settings
2. Executes the script
3. Consults the calculated result

## 🚀 VS Code Extensions

<img width="255" height="218" alt="extensions" src="https://github.com/user-attachments/assets/760eff19-8eaf-429f-ba2b-f1b03c61ead7" />

---

## 📝 Notas

- Os valores monetários estão todos em **euros (EUR)**.
- As percentagens (`*_PCT`) devem ser indicadas como número, por exemplo `28` para 28 %.
