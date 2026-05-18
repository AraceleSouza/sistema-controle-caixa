def calcular_saldo_total(caixa):
    return (
        caixa["dinheiro"]
        + caixa["cartao"]
        + caixa["pix"]
    )


def formatar_moeda(valor):
    return f"R$ {valor:.2f}"