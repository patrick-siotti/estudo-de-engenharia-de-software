# ---- Estágio 1: O Construtor (Builder) ----
FROM python:3.13-slim AS builder

WORKDIR /app

# Instala o Poetry
RUN pip install --no-cache-dir poetry

# Desativa a criação de venvs
RUN poetry config virtualenvs.create false

# Copia os arquivos de configuração e instala as dependências
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --without dev

# Copia todo o conteúdo da sua pasta 'src' para o diretório de trabalho do builder
# Agora, teremos a estrutura /app/projeto_previsao/
COPY ./src/ .


# ---- Estágio 2: A Imagem Final (Final) ----
FROM python:3.13-slim AS final

# Define o diretório de trabalho final
WORKDIR /app

# Copia as dependências instaladas do estágio 'builder'
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages

# Copia nosso código fonte do estágio 'builder'
# A estrutura final será /app/projeto_previsao/
COPY --from=builder /app/projeto_previsao ./projeto_previsao

# --- A CORREÇÃO ESTÁ AQUI ---
# Adiciona o diretório de trabalho '/app' ao PYTHONPATH.
# Agora, Python saberá onde encontrar o pacote 'projeto_previsao'.
ENV PYTHONPATH="/app"

# Define o comando que será executado quando o contêiner iniciar
CMD ["python", "-m", "projeto_previsao"]