FROM python:3.9

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar extensões do VSCode
RUN pip install flake8 black

# Configurar diretório de trabalho
WORKDIR /workspace

# Copiar e instalar requisitos
COPY requirements.txt /workspace/
RUN pip install -r requirements.txt

# Copiar todo o projeto
COPY . /workspace/
