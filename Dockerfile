# Description: Dockerfile for the Flask app
FROM python:3.9-slim

WORKDIR /app

COPY app/ /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]