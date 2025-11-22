from fastapi import APIRouter, Depends
from typing import List
from .. import schemas

router = APIRouter(
    prefix="/search",
    tags=["search"],
)

@router.post("/kipris", response_model=List[schemas.SearchResult])
def search_kipris(query: schemas.SearchQuery):
    # Mock implementation for MVP
    # TODO: Integrate real KIPRIS API
    mock_results = [
        schemas.SearchResult(
            title=f"Mock Patent for {k}",
            abstract="This is a mock abstract for the patent.",
            publication_number=f"KR-2023-{i:04d}",
            applicant="Mock Company Ltd.",
            publication_date="2023-01-01"
        )
        for i, k in enumerate(query.keywords)
    ]
    return mock_results
