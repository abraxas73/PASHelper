from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..main import app
from ..database import Base, get_db
import pytest

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to PASHelper API"}

def test_create_project():
    response = client.post(
        "/projects/",
        json={
            "title": "Test Project",
            "invention_title": "Test Invention",
            "technical_field": "Test Field",
            "problem_to_solve": "Test Problem",
            "technical_solution": "Test Solution"
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Project"
    assert "id" in data

def test_search_kipris():
    response = client.post(
        "/search/kipris",
        json={"keywords": ["AI", "Patent"]},
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert "Mock Patent" in data[0]["title"]
