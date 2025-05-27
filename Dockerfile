FROM python:3.11-alpine

# Install minimal ffmpeg
RUN apk add --no-cache ffmpeg

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8700

CMD ["python", "app.py"] 