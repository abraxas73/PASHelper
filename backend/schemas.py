from pydantic import BaseModel
from typing import List, Optional, Any
from datetime import datetime

# User Schemas
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

# Project Schemas
class ProjectBase(BaseModel):
    title: str
    invention_title: str
    technical_field: str
    problem_to_solve: str
    technical_solution: str
    key_features: List[Any] = []

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    user_id: int
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

# Search Schemas
class SearchQuery(BaseModel):
    keywords: List[str]
    boolean_expression: Optional[str] = None

class SearchResult(BaseModel):
    title: str
    abstract: str
    publication_number: str
    applicant: str
    publication_date: str
