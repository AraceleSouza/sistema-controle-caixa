from datetime import datetime

from flask import Flask, jsonify, render_template, request

from utils.helpers import calcular_saldo_total, formatar_moeda

app = Flask(__name__)

caixa = {
    "dinheiro": 0,
    "cartao": 0,
    "pix": 0
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/processar", methods=["POST"])
def processar_venda():
    try:
        dados = request.get_json()

        valor_compra = float(dados.get("valor", 0))
        forma_pagamento = dados.get("pagamento", "").lower()

        if valor_compra <= 0:
            return jsonify({"erro": "Informe um valor válido"}), 400

        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        resposta = {
            "data_hora": data_hora
        }

        if forma_pagamento == "dinheiro":

            valor_pago = float(dados.get("pago", 0))

            if valor_pago < valor_compra:
                return jsonify({"erro": "Valor insuficiente"}), 400

            troco = valor_pago - valor_compra

            caixa["dinheiro"] += valor_compra

            resposta["mensagem"] = "Venda realizada em dinheiro"
            resposta["detalhes"] = (
                f"Pago: {formatar_moeda(valor_pago)} | "
                f"Troco: {formatar_moeda(troco)}"
            )

        elif forma_pagamento == "credito":

            taxa = valor_compra * 0.05
            valor_total = valor_compra + taxa

            caixa["cartao"] += valor_total

            resposta["mensagem"] = "Venda realizada no crédito"
            resposta["detalhes"] = (
                f"Taxa de 5%: {formatar_moeda(taxa)}"
            )

        elif forma_pagamento == "debito":

            caixa["cartao"] += valor_compra

            resposta["mensagem"] = "Venda realizada no débito"
            resposta["detalhes"] = "Pagamento aprovado"

        elif forma_pagamento == "pix":

            caixa["pix"] += valor_compra

            resposta["mensagem"] = "Pagamento via PIX realizado"
            resposta["detalhes"] = "Transferência confirmada"

        else:
            return jsonify({"erro": "Forma de pagamento inválida"}), 400

        resposta["valor"] = valor_compra
        resposta["pagamento"] = forma_pagamento

        resposta["saldo"] = calcular_saldo_total(caixa)
        resposta["dinheiro"] = caixa["dinheiro"]
        resposta["cartao"] = caixa["cartao"]
        resposta["pix"] = caixa["pix"]

        return jsonify(resposta)

    except ValueError:
        return jsonify({"erro": "Valor inválido"}), 400

    except Exception as erro:
        print("ERRO:", erro)
        return jsonify({"erro": "Erro interno do servidor"}), 500


if __name__ == "__main__":
    app.run(debug=True)