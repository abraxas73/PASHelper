# 시스템 아키텍처 (System Architecture)

## 개요 (Overview)
PASHelper는 특허 선행 기술 조사(Prior Art Search)를 지원하기 위해 설계된 웹 어플리케이션입니다.
Next.js로 구축된 최신 프론트엔드와 FastAPI 기반의 강력한 백엔드로 구성되어 있습니다.

## 기술 스택 (Tech Stack)

### Frontend
- **프레임워크**: Next.js 14 (App Router)
- **언어**: TypeScript
- **스타일링**: Tailwind CSS
- **상태 관리**: React Hooks (로컬 상태), Context API (필요 시)
- **HTTP 클라이언트**: Native `fetch` API

### Backend
- **프레임워크**: FastAPI
- **언어**: Python 3.11+
- **데이터베이스**: PostgreSQL (운영/개발), SQLite (테스트)
- **ORM**: SQLAlchemy
- **스키마 검증**: Pydantic

### 인프라 (Infrastructure)
- **컨테이너화**: Docker & Docker Compose
- **데이터베이스**: PostgreSQL 15

## 디렉토리 구조 (Directory Structure)

```
PASHelper/
├── backend/                # Python FastAPI 백엔드
│   ├── routers/            # API 라우트 핸들러
│   ├── tests/              # Pytest 테스트
│   ├── crud.py             # 데이터베이스 CRUD 작업
│   ├── database.py         # 데이터베이스 연결 설정
│   ├── main.py             # 어플리케이션 진입점
│   ├── models.py           # SQLAlchemy 모델
│   ├── schemas.py          # Pydantic 스키마
│   └── requirements.txt    # Python 의존성
├── frontend/               # Next.js 프론트엔드
│   ├── src/
│   │   ├── app/            # App Router 페이지
│   │   ├── components/     # 재사용 가능한 UI 컴포넌트
│   │   └── lib/            # 유틸리티 (API 클라이언트 등)
│   └── package.json        # Node.js 의존성
├── docs/                   # 문서
├── scripts/                # 유틸리티 스크립트
└── docker-compose.yml      # Docker 오케스트레이션
```

## 데이터 모델 (Data Model)

### User (사용자)
- 등록된 사용자를 나타냅니다.
- 필드: `email`, `hashed_password`, `is_active`.

### Project (프로젝트)
- 특허 조사 프로젝트를 나타냅니다.
- 필드: `title` (프로젝트명), `invention_title` (발명의 명칭), `technical_field` (기술 분야), `problem_to_solve` (해결 과제), `key_features` (핵심 기술).
- 관계: User에 속함.

### SearchSession (검색 세션 - 예정)
- 검색 이력 및 결과를 저장합니다.

### PriorArt (선행 기술 - 예정)
- 발견된 특허 및 분석 내용을 저장합니다.

## API 설계 (API Design)

### Projects
- `GET /projects`: 모든 프로젝트 목록 조회.
- `POST /projects`: 새 프로젝트 생성.
- `GET /projects/{id}`: 프로젝트 상세 조회.

### Search
- `POST /search/kipris`: 특허 검색 (현재는 Mock 구현).

### Auth
- `POST /auth/register`: 새 사용자 등록.
