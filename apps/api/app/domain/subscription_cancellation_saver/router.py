from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.subscription_cancellation_saver.schemas import AgenticSubscriptionCancellationSaverSessionCreate, AgenticSubscriptionCancellationSaverSessionResponse
from app.domain.subscription_cancellation_saver.service import AgenticSubscriptionCancellationSaverService

router = APIRouter(prefix="/api/v1/subscription_cancellation_saver", tags=["Agentic Subscription Cancellation Saver Domain"])

@router.post("/sessions", response_model=AgenticSubscriptionCancellationSaverSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticSubscriptionCancellationSaverSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Subscription Cancellation Saver.
    """
    return AgenticSubscriptionCancellationSaverService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticSubscriptionCancellationSaverSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticSubscriptionCancellationSaverService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
