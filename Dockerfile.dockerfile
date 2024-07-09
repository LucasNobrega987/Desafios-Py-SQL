# imagem base do Python
FROM python:3.8-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho
COPY requirements.txt requirements.txt
COPY app.py app.py

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# coloque a porta que a aplicação Flask usa
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["python", "app.py"]
