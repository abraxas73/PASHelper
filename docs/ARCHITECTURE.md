# System Architecture

## Overview
PASHelper is a web application designed to assist with Prior Art Search for patents.
It consists of a modern frontend built with Next.js and a robust backend powered by FastAPI.

## Tech Stack

### Frontend
- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State Management**: React Hooks (local state), Context API (if needed)
- **HTTP Client**: Native `fetch` API

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.11+
- **Database**: PostgreSQL (Production/Dev), SQLite (Testing)
- **ORM**: SQLAlchemy
- **Schema Validation**: Pydantic

### Infrastructure
- **Containerization**: Docker & Docker Compose
- **Database**: PostgreSQL 15

## Directory Structure

```
PASHelper/
├── backend/                # Python FastAPI Backend
│   ├── routers/            # API Route handlers
│   ├── tests/              # Pytest tests
│   ├── crud.py             # Database CRUD operations
│   ├── database.py         # Database connection setup
│   ├── main.py             # Application entry point
│   ├── models.py           # SQLAlchemy models
│   ├── schemas.py          # Pydantic schemas
│   └── requirements.txt    # Python dependencies
├── frontend/               # Next.js Frontend
│   ├── src/
│   │   ├── app/            # App Router pages
│   │   ├── components/     # Reusable UI components
│   │   └── lib/            # Utilities (API client, etc.)
│   └── package.json        # Node.js dependencies
├── docs/                   # Documentation
├── scripts/                # Utility scripts
└── docker-compose.yml      # Docker orchestration
```

## Data Model

### User
- Represents a registered user.
- Fields: `email`, `hashed_password`, `is_active`.

### Project
- Represents a patent search project.
- Fields: `title`, `invention_title`, `technical_field`, `problem_to_solve`, `key_features`.
- Relationships: Belongs to a User.

### SearchSession (Planned)
- Stores search history and results.

### PriorArt (Planned)
- Stores found patents and analysis.

## API Design

### Projects
- `GET /projects`: List all projects.
- `POST /projects`: Create a new project.
- `GET /projects/{id}`: Get project details.

### Search
- `POST /search/kipris`: Search for patents (currently mocked).

### Auth
- `POST /auth/register`: Register a new user.
