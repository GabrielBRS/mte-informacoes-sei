# Estágio 1: Build leve
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia apenas os requisitos de produção
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia apenas o código fonte necessário (ignora research e data)
COPY src/ /app/src/

# Define a variável de ambiente para o Python encontrar os módulos
ENV PYTHONPATH=/app/src

# Expõe a porta da FastAPI
EXPOSE 8000

# Comando para rodar com Uvicorn
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
