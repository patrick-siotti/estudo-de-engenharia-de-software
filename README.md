# Projeto Previsão - Estudo de Engenharia de Software com Python

![Status: Estudo Concluído](https://img.shields.io/badge/status-estudo%20concluído-brightgreen)
![Python: 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Poetry](https://img.shields.io/badge/packaging-poetry-cyan.svg)
![Pytest](https://img.shields.io/badge/testing-pytest-blueviolet.svg)
![Docker](https://img.shields.io/badge/container-docker-blue.svg)

## 📄 Sobre o Projeto

Este é um projeto de estudo que consiste em uma simples aplicação de linha de comando para análise de previsão do tempo. O objetivo principal não era criar uma aplicação complexa, mas sim aplicar e documentar um fluxo de trabalho de engenharia de software moderno e robusto utilizando Python.

O foco foi construir uma base sólida, seguindo as melhores práticas de mercado para qualidade de código, gerenciamento de dependências, testes e distribuição.

---

## 🏛️ Arquitetura e Filosofia do Projeto

Cada ferramenta e prática neste projeto foi escolhida com um propósito claro, visando criar um software que seja **confiável, manutenível e reprodutível**.

### 1. Qualidade e Robustez do Código

A base para um bom software é um código que inspira confiança e é fácil de entender.

* **Tipagem Estática (`mypy`)**: O projeto é 100% tipado. Utilizamos as anotações de tipo do Python e a ferramenta `mypy` para análise estática.
    * **Por quê?** Para encontrar bugs relacionados a tipos *antes* da execução, tornar o código auto-documentado e permitir que editores de código ofereçam um autocompletar mais inteligente e refatorações mais seguras.

* **Testes Automatizados (`pytest`)**: A lógica de negócio é coberta por uma suíte de testes automatizados.
    * **Por quê?** Para garantir que a aplicação se comporte como o esperado e para criar uma "rede de segurança" que nos permita adicionar novas funcionalidades ou refatorar o código existente sem medo de quebrar o que já funciona. Usamos `pytest-mock` para isolar o código de dependências externas.

### 2. Gerenciamento e Reprodutibilidade

Um dos maiores desafios no desenvolvimento é garantir que um projeto funcione da mesma forma em diferentes ambientes.

* **Poetry**: O gerenciamento de dependências e de ambiente virtual é feito com o Poetry.
    * **Por quê?** O Poetry resolve o clássico problema do "na minha máquina funciona". O arquivo `poetry.lock` garante que todos os desenvolvedores e o ambiente de produção usem as **versões exatas** de todas as dependências, garantindo um ambiente de desenvolvimento idêntico para todos.

* **Docker**: A aplicação é totalmente containerizada.
    * **Por quê?** O Docker leva a reprodutibilidade a um novo nível. Ele empacota a aplicação, a versão exata do Python, as bibliotecas do sistema e todas as dependências em um **contêiner isolado**. Isso garante que a aplicação rode de forma idêntica em qualquer máquina que tenha Docker, seja no desenvolvimento, em testes ou na produção final.

### 3. Estrutura do Projeto

* **Layout `src`**: O código-fonte reside dentro de um diretório `src`.
    * **Por quê?** É uma prática recomendada que previne uma série de problemas comuns de importação em Python e deixa uma separação clara entre o código do pacote e os arquivos de configuração do projeto.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.13
* **Gerenciamento de Pacotes:** Poetry
* **Testes:** Pytest, Pytest-Mock
* **Análise de Tipos:** Mypy
* **Containerização:** Docker & Docker Compose

---

## 🚀 Como Executar o Projeto

Você pode executar o projeto de duas maneiras: localmente com Poetry ou via Docker (recomendado para uma demonstração rápida).

### Pré-requisitos

* Git
* Python 3.13+
* Poetry
* Docker e Docker Compose

### 1. Executando com Docker (Recomendado)

Este é o método mais simples e garante que tudo funcione sem a necessidade de gerenciar ambientes Python locais.

```bash
# 1. Clone o repositório
git clone [https://github.com/seu-usuario/projeto_previsao.git](https://github.com/seu-usuario/projeto_previsao.git)
cd projeto_previsao

# 2. Construa a imagem Docker
docker build -t previsao-app .

# 3. Execute o contêiner
docker run --rm previsao-app
```

### 2. Executando Localmente com Poetry

Este método é ideal para desenvolvimento e para rodar os testes.

```bash
# 1. Clone o repositório
git clone [https://github.com/seu-usuario/projeto_previsao.git](https://github.com/seu-usuario/projeto_previsao.git)
cd projeto_previsao

# 2. Instale as dependências
# (O Poetry criará um ambiente virtual automaticamente)
poetry install

# 3. Execute os testes para garantir que tudo está ok
poetry run pytest

# 4. Execute a aplicação
poetry run python -m projeto_previsao
```