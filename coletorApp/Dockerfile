# 1️⃣ Base
FROM python:3.11-slim
LABEL build_version="1.0.4-opencv-fix"

# 2️⃣ Configurações básicas
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLET_DISPLAY=false
ENV APP_HOME=/app
WORKDIR $APP_HOME

# 3️⃣ Instalar dependências do sistema necessárias pro OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 4️⃣ Copiar o código e dependências
COPY ./src ./src
COPY requirements.txt ./

# 5️⃣ Instalar pacotes Python
RUN pip install --no-cache-dir -r requirements.txt

# 6️⃣ Criar pastas
RUN mkdir -p data reports

# 7️⃣ Expor porta
EXPOSE 8080

# 8️⃣ Rodar o app Flet
CMD ["python", "src/main.py"]
