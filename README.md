# mte-informacoes-sei

# Executado na raiz do projeto
docker build -t api-sei-linuxell -f infra/Dockerfile .


gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000
