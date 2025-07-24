# ---- Estágio 1: O Construtor (Builder) ----
# Usamos uma imagem oficial do Python. A tag 'slim' é uma versão menor.
# Damos um "apelido" para este estágio: 'builder'.
FROM python:3.11-slim as builder

# Define o diretório de trabalho dentro do contêiner.
WORKDIR /app

# Instala o Poetry no ambiente do builder.
# A flag --no-cache-dir é uma boa prática para manter a imagem menor.
RUN pip install --no-cache-dir poetry

# Copia apenas os arquivos de configuração primeiro.
# O Docker armazena em cache cada passo. Se estes arquivos não mudarem,
# o Docker reutiliza o cache do passo seguinte, tornando o build muito mais rápido.
COPY pyproject.toml poetry.lock ./

# Instala apenas as dependências de PRODUÇÃO.
# --no-dev: ignora pytest, mypy, etc.
# --no-root: não instala o projeto em si, apenas suas dependências.
RUN poetry install --no-dev --no-root

# Agora, copia todo o nosso código fonte.
COPY ./src/projeto_previsao ./src/projeto_previsao


# ---- Estágio 2: A Imagem Final (Final) ----
# Começamos de novo com uma imagem limpa para manter a imagem final pequena.
FROM python:3.11-slim as final

WORKDIR /app

# Copia o ambiente virtual com as dependências já instaladas do estágio 'builder'.
COPY --from=builder /app/.venv ./.venv

# Copia o nosso código fonte do estágio 'builder'.
COPY --from=builder /app/src/projeto_previsao ./src/projeto_previsao

# "Ativa" o ambiente virtual adicionando-o ao PATH do sistema no contêiner.
ENV PATH="/app/.venv/bin:$PATH"

# Define o comando que será executado quando o contêiner iniciar.
# É o mesmo comando que usamos no terminal!
CMD ["python", "-m", "projeto_previsao"]