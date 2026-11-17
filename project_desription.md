# 📈 Personal Project

Personal calculator to estimate the **net value** of selling a position, taking into account commissions, withdrawal fees, and capital gains tax (IRS).

---

## ⚙️ Configuration

Define const on the top of the script

| Constant | Description |
|---|---|
| `QUANTITY` | Number of units held |
| `AVERAGE_PRICE_EUR` | Average purchase price, in euros |
| `TICKER` | Asset symbol (e.g., `AAPL`) |
| `MANUAL_PRICE_EUR` | Manual price, in euros (used when automatic quote is not available) |
| `SELL_COMMISSION_PCT` | Selling commission, in percentage |
| `SELL_COMMISSION_MIN` | Minimum selling commission, in euros |
| `WITHDRAWAL_FEE_EUR` | Withdrawal fee, in euros |
| `IRS_RATE_PCT` | Capital gains tax rate (IRS), in percentage |

### const

```text
const QUANTITY
const AVERAGE_PRICE_EUR
const TICKER
const MANUAL_PRICE_EUR
const SELL_COMMISSION_PCT
const SELL_COMMISSION_MIN
const WITHDRAWAL_FEE_EUR
const IRS_RATE_PCT
```

---

## 🧩 Python Methods

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

<img width="255" height="218" alt="extensions" src="https://github.com/user-attachments/assets/herethename"

---
## 📝 Telegram bot

<img width="255" height="218" alt="extensions" src="https://github.com/user-attachments/assets/760eff19-8eaf-429f-ba2b-f1b03c61ead7"

## 📝 Notes

- Currency in **EUR**.
- Percentage should be a number (`*_PCT`) such as por `28` to 28 %.
