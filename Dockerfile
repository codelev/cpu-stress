FROM python:3.11-slim
WORKDIR /app
COPY app.py .
ENTRYPOINT ["python", "app.py"]
