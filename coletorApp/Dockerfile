# 1️⃣ Base
FROM python:3.11-slim
LABEL build_version="1.0.3-final-asgi-fix"

# 2️⃣ Configurações básicas
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLET_DISPLAY=false
ENV APP_HOME=/app
WORKDIR $APP_HOME

# 3️⃣ Copiar o código
COPY ./src ./src
COPY requirements.txt ./

# 4️⃣ Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Criar pastas de dados
RUN mkdir -p data reports

# 6️⃣ Expor porta (Render usa variáveis de ambiente)
EXPOSE 8080

# 7️⃣ Comando para iniciar o app
CMD ["python", "src/main.py"]
