FROM python:3.11-alpine

# Install minimal ffmpeg and build dependencies
RUN apk add --no-cache ffmpeg \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev \
    cargo

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8700

CMD ["python", "app.py"] 