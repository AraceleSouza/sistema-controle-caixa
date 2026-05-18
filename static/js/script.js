const botaoVenda = document.getElementById("botao-venda");

document.addEventListener("DOMContentLoaded", () => {

    atualizarRelogio();

    setInterval(atualizarRelogio, 1000);

    configurarFormaPagamento();

    botaoVenda.addEventListener("click", processarVenda);
});

function atualizarRelogio() {

    const agora = new Date();

    document.getElementById("data").innerText =
        agora.toLocaleDateString("pt-BR");

    document.getElementById("hora").innerText =
        agora.toLocaleTimeString("pt-BR");
}

function configurarFormaPagamento() {

    const pagamentoSelect = document.getElementById("pagamento");

    pagamentoSelect.addEventListener("change", () => {

        const campoExtra = document.getElementById("campo-extra");

        campoExtra.innerHTML = "";

        if (pagamentoSelect.value === "dinheiro") {

            campoExtra.innerHTML = `
                <label for="valorPago">
                    Valor pago pelo cliente
                </label>

                <input
                    type="number"
                    id="valorPago"
                    placeholder="0.00"
                    step="0.01"
                >
            `;
        }
    });
}

async function processarVenda() {

    try {

        botaoVenda.disabled = true;
        botaoVenda.innerText = "Processando...";

        const valorInput = document.getElementById("valor");
        const pagamentoSelect = document.getElementById("pagamento");

        const valor = parseFloat(valorInput.value);

        const pagamento = pagamentoSelect.value;

        const dadosVenda = {
            valor,
            pagamento
        };

        if (pagamento === "dinheiro") {

            const valorPago =
                parseFloat(document.getElementById("valorPago").value);

            dadosVenda.pago = valorPago;
        }

        const resposta = await fetch("/processar", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(dadosVenda)
        });

        const resultado = await resposta.json();

        if (!resposta.ok) {
            mostrarMensagem(resultado.erro, "erro");
            return;
        }

        atualizarResumo(resultado);

        adicionarHistorico(resultado);

        mostrarMensagem(
            "Venda registrada com sucesso!",
            "sucesso"
        );

        limparFormulario();

    } catch (erro) {

        console.error(erro);

        mostrarMensagem(
            "Erro ao processar venda",
            "erro"
        );

    } finally {

        botaoVenda.disabled = false;
        botaoVenda.innerText = "Confirmar Venda";
    }
}

function atualizarResumo(resultado) {

    document.getElementById("saldo").innerText =
        formatarMoeda(resultado.saldo);

    document.getElementById("dinheiro").innerText =
        formatarMoeda(resultado.dinheiro);

    document.getElementById("cartao").innerText =
        formatarMoeda(resultado.cartao);

    document.getElementById("pix").innerText =
        formatarMoeda(resultado.pix);
}

function adicionarHistorico(resultado) {

    const historico = document.getElementById("historico");

    historico.innerHTML += `
        <tr>
            <td>${resultado.data_hora}</td>

            <td>
                <span class="tag ${resultado.pagamento}">
                    ${resultado.pagamento}
                </span>
            </td>

            <td>${resultado.detalhes}</td>

            <td class="valor">
                ${formatarMoeda(resultado.valor)}
            </td>
        </tr>
    `;
}

function mostrarMensagem(texto, tipo) {

    const mensagem = document.getElementById("mensagem");

    mensagem.innerText = texto;

    mensagem.className = tipo;

    setTimeout(() => {
        mensagem.innerText = "";
        mensagem.className = "";
    }, 3000);
}

function limparFormulario() {

    document.getElementById("valor").value = "";

    document.getElementById("campo-extra").innerHTML = "";
}

function formatarMoeda(valor) {

    return valor.toLocaleString("pt-BR", {

        style: "currency",

        currency: "BRL"
    });
}