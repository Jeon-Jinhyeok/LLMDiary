#!/bin/sh

echo "Waiting for PostgreSQL..."

# PostgreSQL이 실행될 때까지 대기
for i in {1..10}; do
  if nc -z db 5432; then
    echo "PostgreSQL started"
    break
  fi
  echo "Waiting for DB to start... ($i/10)"
  sleep 1
done

# 마이그레이션 적용
python manage.py migrate --noinput

# 정적 파일 수집
python manage.py collectstatic --noinput

echo "============================================"
echo "✅ Django Server is running successfully!"
echo "🌍 Open in your browser: http://localhost:8000"
echo "============================================"

# Gunicorn이 설치되지 않았다면 runserver로 실행
if ! command -v gunicorn &> /dev/null; then
  echo "Gunicorn not found, running Django's built-in server instead..."
  exec python manage.py runserver 0.0.0.0:8000
else
  echo "Starting Gunicorn..."
  exec gunicorn emotion_diary.wsgi:application --bind 0.0.0.0:8000
fi
