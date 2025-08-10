FROM python:3.13.5-alpine3.22
LABEL maintainer="github.com/rubemvn"

# Desativa a criação de arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Python imprime logs imediatamente (sem buffer)
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho
WORKDIR /app

# Copia todo o projeto para /app
COPY . /app

# Copia scripts para /scripts (fora do /app)
COPY scripts /scripts

# Expõe a porta 8000 (usada pelo Django)
EXPOSE 8000

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r requirements.txt && \
  adduser --disabled-password --no-create-home duser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R duser:duser /venv && \
  chown -R duser:duser /data/web/static && \
  chown -R duser:duser /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts


# Ajusta PATH para incluir scripts e o virtualenv em /app/venv/bin
ENV PATH="/scripts:/venv/bin:$PATH"

# Usa o usuário não-root criado para rodar a aplicação
USER duser

# Comando padrão: executa o script de comandos
CMD ["sh", "/scripts/commands.sh"]
