# ==============================
# 🐍 Coletor App - Dockerfile
# Compatível com Render.com
# Versão: 1.0.4-opencv-fix
# ==============================

# 1️⃣ Imagem base
FROM python:3.11-slim
LABEL build_version="1.0.4-opencv-fix"

# 2️⃣ Configuração do ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLET_DISPLAY=false
ENV APP_HOME=/app
WORKDIR $APP_HOME

# 3️⃣ Instalar dependências do sistema (necessárias pro OpenCV)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 4️⃣ Copiar código do app e dependências
COPY ./src ./src
COPY requirements.txt ./

# 5️⃣ Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# 6️⃣ Criar diretórios para dados e relatórios
RUN mkdir -p data reports

# 7️⃣ Expor a porta usada pelo Render (Render usa variável $PORT)
EXPOSE 8080

# 8️⃣ Comando para rodar o app (Render usa CMD automaticamente)
CMD ["python", "src/main.py"]
