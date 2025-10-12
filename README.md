# Lojinha da Lulu  🛍️

## **:computer:** Sobre o Projeto

Um projeto simples em Python para **registro de vendas** com diferentes formas de pagamento: dinheiro, cartão (débito ou crédito) e pix.  
O sistema exibe totais por tipo de pagamento, calcula acréscimos e troco, e mantém um saldo geral do caixa.

## 🛠️ Tecnologias Utilizadas

-   Python 3  
-   Módulo `time`
-   ANSI Escape Codes (para cores no terminal)

##  **:sparkles:** Funcionalidades

-   Registrar novas vendas.
-   Calcular o total de vendas realizadas.
-  Listar  total de vendas por tipo de pagamento (cartão, pix ou dinheiro).
- Aplicar regras específicas conforme o tipo de pagamento:
-   💳 **Cartão de crédito:** acréscimo de **5%** sobre o valor total.
-   💳 **Cartão de débito:** valor sem acréscimo.
-   💸 **Dinheiro:** informa o **valor pago** e calcula o **troco**.
-   ⚡ **Pix:** valor sem acréscimo.
-   Interface em linha de comando (CLI) simples e intuitiva.


## 🧠 Conceitos utilizados

- Estrutura do Programa.
- Entrada de Dados.
- Estruturas Condicionais.
- Manipulação de Strings.
- Cálculos com Porcentagem e Troco.
- Variáveis Acumuladoras.
- Formatação de Saída.
- Cores no Terminal (ANSI).
- Biblioteca `time`.


## ⚙️ Funcionamento do Sistema

1.  O sistema mostra o nome da loja centralizado na tela.
2.  Solicita o valor da compra.
3.  Exibe as opções de pagamento:
    -   `[1]` Dinheiro
    -   `[2]` Cartão (D/C)
    -   `[3]` Pix
4.  Calcula e mostra o resultado conforme a forma de pagamento:
    -   **Dinheiro:** solicita valor pago e calcula troco.
    -   **Cartão de crédito:** adiciona acréscimo de 5%.
    -   **Cartão de débito:** valor normal.
    -   **Pix:** valor normal.
5.  Acumula os valores nas variáveis correspondentes.
6.  Pergunta se deseja registrar uma nova compra.
7.  Ao encerrar, mostra o **saldo total** e o **total de vendas por tipo de pagamento**.


## 🎯 Objetivo

Criar uma aplicação prática e didática para reforçar o aprendizado de **Python básico** e **lógica de programação**, simulando o funcionamento de um pequeno sistema de controle de vendas.