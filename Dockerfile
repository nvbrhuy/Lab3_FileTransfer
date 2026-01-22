FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY watcher.py .
CMD ["python", "watcher.py"]
