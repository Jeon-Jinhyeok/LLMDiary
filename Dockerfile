FROM python:3.10

WORKDIR /app

# 시스템 패키지 설치 (netcat 및 PostgreSQL 클라이언트 포함)
RUN apt-get update --fix-missing && apt-get install -y \
    netcat-traditional \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# 의존성 파일 복사 후 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 코드 복사
COPY . .

# 실행 권한 부여
RUN chmod +x /app/start.sh

# Django 실행 (start.sh 사용)
ENTRYPOINT ["/bin/sh", "-c", "/app/start.sh"]
