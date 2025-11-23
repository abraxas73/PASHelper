from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Float, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    projects = relationship("Project", back_populates="owner")

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, index=True)
    invention_title = Column(String)
    technical_field = Column(String)
    problem_to_solve = Column(Text)
    technical_solution = Column(Text)
    key_features = Column(JSON) # List of KeyFeature objects
    status = Column(String, default="IN_PROGRESS")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    owner = relationship("User", back_populates="projects")
    search_sessions = relationship("SearchSession", back_populates="project")
    prior_arts = relationship("PriorArt", back_populates="project")
    reports = relationship("Report", back_populates="project")

class SearchSession(Base):
    __tablename__ = "search_sessions"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    search_query = Column(JSON) # SearchQuery object
    results = Column(JSON) # List of SearchResult objects (simplified for MVP)
    total_count = Column(Integer)
    executed_at = Column(DateTime(timezone=True), server_default=func.now())

    project = relationship("Project", back_populates="search_sessions")

class PriorArt(Base):
    __tablename__ = "prior_arts"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    type = Column(String) # PATENT, PAPER, OTHER
    
    # Patent Info
    publication_number = Column(String)
    application_number = Column(String)
    title = Column(String)
    abstract = Column(Text)
    claims = Column(JSON)
    applicant = Column(String)
    inventor = Column(String)
    filing_date = Column(DateTime)
    publication_date = Column(DateTime)
    ipc_codes = Column(JSON)
    country = Column(String)

    # Analysis
    relevance_score = Column(Float)
    feature_mapping = Column(JSON)
    user_notes = Column(Text)
    status = Column(String) # RELEVANT, NOT_RELEVANT, REVIEW_NEEDED

    project = relationship("Project", back_populates="prior_arts")

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    type = Column(String)
    content = Column(JSON)
    generated_at = Column(DateTime(timezone=True), server_default=func.now())
    format = Column(String)
    file_url = Column(String)

    project = relationship("Project", back_populates="reports")
