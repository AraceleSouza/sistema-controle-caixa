# 🛍️ Lojinha da Lulu

## 💻 Sobre o Projeto

Este projeto é um sistema simples de registro de vendas desenvolvido em Python, executado via terminal.
A aplicação permite registrar compras utilizando diferentes formas de pagamento, calcular valores automaticamente e manter o controle do caixa.

---

## 🚀 Funcionalidades

* 🧾 Registro de vendas
* 💰 Cálculo do valor total das vendas
* 📊 Controle de vendas por tipo de pagamento
* 💳 Regras específicas por pagamento:

  * Crédito: acréscimo de 5%
  * Débito: valor normal
  * Pix: valor normal
  * Dinheiro: cálculo de troco
* 🧮 Controle de saldo total do caixa
* 🧭 Interface simples via terminal (CLI)

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Módulo padrão `time`
* ANSI Escape Codes (cores no terminal)

---

## ▶️ Como Executar o Projeto

1. Execute o arquivo principal:

```bash id="loja1"
python main.py
```

2. Siga as instruções exibidas no terminal.

---

## ⚙️ Funcionamento do Sistema

1. Exibe o nome da loja
2. Solicita o valor da compra
3. Apresenta as opções de pagamento:

   * `[1]` Dinheiro
   * `[2]` Cartão (Crédito/Débito)
   * `[3]` Pix
4. Aplica regras conforme o pagamento
5. Registra e acumula os valores
6. Permite múltiplas vendas
7. Exibe resumo final do caixa

---

## 🧠 Conceitos Aplicados

* Estruturas condicionais
* Laços de repetição
* Manipulação de strings
* Cálculo de porcentagem
* Variáveis acumuladoras
* Formatação de saída
* Uso de cores no terminal (ANSI)
* Controle de fluxo do programa

---

## 📌 Observações

* Os dados são armazenados apenas em memória
* O sistema é executado via terminal
* Não há persistência em banco de dados

---

## 🔮 Melhorias Futuras

* 💾 Persistência de dados (arquivo ou banco)
* 📄 Geração de relatório de vendas
* 🖥️ Interface gráfica
* 🌐 Versão web
* 📅 Histórico de vendas

---

## 🎯 Objetivo

Desenvolver uma aplicação prática para consolidar conhecimentos em lógica de programação, estruturas de controle e manipulação de dados em Python, simulando um sistema real de vendas.

---

## 👩‍💻 Autora

Aracele Souza
Estudante de Engenharia de Software em transição de carreira para desenvolvimento
