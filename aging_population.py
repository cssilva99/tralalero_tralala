#!/usr/bin/env python3
"""
Lucro/prejuízo líquido do ETF iShares Ageing Population (XTB), em euros,
já com taxas de venda, de levantamento e IRS descontados.

Instalar:   pip install yfinance
Executar:   python etf_diario.py
"""
import yfinance as yf

# ----------------- OS TEUS DADOS (do ecrã "My trades" da XTB) -----------------
QUANTIDADE = 88.2777
PRECO_MEDIO_EUR = 9.0407

# Ticker no Yahoo Finance da cotação em EUR (Xetra). Confirma pelo ISIN IE00B1TXLS18
# que o preço bate com o da XTB.
TICKER = "2B77.DE"

# Se o Yahoo falhar ou não bater certo com a XTB, preenche o preço atual (em EUR)
# visto na app e o script usa-o em vez do Yahoo. Deixa None para usar o Yahoo.
PRECO_MANUAL_EUR = None

# ----------------- TAXAS (confirma em xtb.com/pt/conta-e-taxas) -----------------
COMISSAO_VENDA_PCT = 0.0      # 0% em ETFs até 100.000 € de volume mensal (depois 0,2%, mín. 10 €)
COMISSAO_VENDA_MIN = 0.0      # põe 10.0 se ultrapassares os 100.000 €/mês
TAXA_LEVANTAMENTO_EUR = 0.0   # taxa fixa em € por levantamento (a XTB indica 0 € acima de 220 €). Altera se pagares alguma

# ----------------- IRS (mais-valias, categoria G) -----------------
# Taxa autónoma geral: 28% sobre o ganho (venda - compra - despesas), só se o ganho for positivo.
# Algumas fontes indicam taxas mais baixas conforme o tempo de detenção
# (25,2% entre 2-5 anos, 22,4% entre 5-8, 19,6% acima de 8); confirma o teu caso.
# Se optares pelo englobamento, a taxa passa a ser a do teu escalão: ajusta aqui.
TAXA_IRS_PCT = 28.0
# ------------------------------------------------------------------------------


def preco_atual_eur():
    if PRECO_MANUAL_EUR is not None:
        return float(PRECO_MANUAL_EUR)
    t = yf.Ticker(TICKER)
    preco = float(t.history(period="5d")["Close"].dropna().iloc[-1])
    moeda = t.fast_info.get("currency", "EUR")
    if moeda == "GBp":          # pence -> libras
        preco, moeda = preco / 100, "GBP"
    if moeda != "EUR":
        fx = yf.Ticker(f"EUR{moeda}=X").history(period="5d")["Close"].dropna().iloc[-1]
        preco = preco / float(fx)
    return preco


def calcular(preco):
    valor_bruto = preco * QUANTIDADE
    custo = PRECO_MEDIO_EUR * QUANTIDADE
    comissao = max(valor_bruto * COMISSAO_VENDA_PCT / 100, COMISSAO_VENDA_MIN) if COMISSAO_VENDA_PCT else 0.0
    # Mais-valia fiscal = venda - compra - despesas da operação (a taxa de levantamento não conta)
    mais_valia = valor_bruto - custo - comissao
    irs = max(mais_valia, 0.0) * TAXA_IRS_PCT / 100
    lucro_liquido = mais_valia - TAXA_LEVANTAMENTO_EUR - irs
    return {
        "valor_bruto": valor_bruto,
        "comissao_venda": comissao,
        "levantamento": TAXA_LEVANTAMENTO_EUR,
        "lucro_antes_irs": mais_valia - TAXA_LEVANTAMENTO_EUR,
        "irs": irs,
        "lucro_liquido": lucro_liquido,
    }


def main():
    r = calcular(preco_atual_eur())
    print(f"Lucro/perda líquido (após taxas, comissões e IRS): {r['lucro_liquido']:+.2f} €")


if __name__ == "__main__":
    main()