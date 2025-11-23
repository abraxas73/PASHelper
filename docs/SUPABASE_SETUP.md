# Supabase 설정 가이드 (Supabase Setup Guide)

## 개요
이 프로젝트는 데이터베이스로 Supabase (Managed PostgreSQL)를 사용합니다.
로컬 개발 환경에서 Supabase에 연결하고 마이그레이션을 적용하는 방법을 설명합니다.

## 사전 준비
1. [Supabase](https://supabase.com/) 계정 생성 및 로그인.
2. 새 프로젝트 생성 (예: `pashelper-dev`).
3. 프로젝트 설정 > Database > Connection Pooling에서 `Transaction` 모드의 Connection String 복사.
   - 예: `postgresql://postgres.xxxx:[YOUR-PASSWORD]@aws-0-ap-northeast-2.pooler.supabase.com:6543/postgres`

## 환경 변수 설정
프로젝트 루트에 `.env` 파일을 생성하고 `DATABASE_URL`을 설정합니다.

```bash
# .env
DATABASE_URL="postgresql://postgres.xxxx:[YOUR-PASSWORD]@aws-0-ap-northeast-2.pooler.supabase.com:6543/postgres"
```

> **주의**: 비밀번호에 특수문자가 포함된 경우 URL 인코딩이 필요할 수 있습니다.

## 데이터베이스 마이그레이션
Alembic을 사용하여 데이터베이스 스키마를 생성/업데이트합니다.

### 1. 마이그레이션 적용 (Upgrade)
Supabase DB에 테이블을 생성하려면 다음 명령어를 실행합니다.

```bash
cd backend
# 가상환경 활성화 (필요시)
# source venv/bin/activate
export DATABASE_URL="[YOUR-SUPABASE-URL]"
python3 -m alembic upgrade head
```

### 2. 새 마이그레이션 생성
모델(`models.py`)을 수정한 후, 변경 사항을 반영하는 마이그레이션 파일을 생성합니다.

```bash
cd backend
export DATABASE_URL="[YOUR-SUPABASE-URL]"
python3 -m alembic revision --autogenerate -m "설명"
```

## 실행
마이그레이션이 완료되면 제공된 스크립트를 사용하여 어플리케이션을 실행합니다.

### 1. 백엔드 실행
```bash
./scripts/restart_backend.sh
```

### 2. 프론트엔드 실행
```bash
./scripts/restart_frontend.sh
```

또는 Docker Compose를 사용할 수도 있습니다.
```bash
docker-compose up --build
```
