# 1. Imagem base do Python
FROM python:3.11-slim

# 2. Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# 3. Copia o arquivo de dependências
COPY requirements.txt .

# 4. Instala as dependências
# (Inclui build-essentials para compilar 'opencv' se necessário)
RUN apt-get update && apt-get install -y build-essential
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia todo o seu código-fonte para o contêiner
# (Isso copia a pasta 'src' inteira para '/app/src')
COPY src/ ./

# 6. Expõe a porta que o app vai usar (definida no src/main.py)
EXPOSE 8080

# 7. Comando para iniciar o app
# (Executa o 'main.py' que está na raiz do WORKDIR, ou seja, /app/main.py)
CMD ["python", "main.py"]