FROM python:3.13-slim

WORKDIR /app

COPY server.py client.py ./

# Expõe a porta que o servidor usará
EXPOSE 8888

# O comando padrão será definido no docker-compose.yml
CMD ["python", "server.py"]