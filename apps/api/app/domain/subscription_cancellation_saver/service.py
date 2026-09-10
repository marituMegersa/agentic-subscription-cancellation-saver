from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.subscription_cancellation_saver.models import AgenticSubscriptionCancellationSaverSession, AgenticSubscriptionCancellationSaverItem
from app.domain.subscription_cancellation_saver.schemas import AgenticSubscriptionCancellationSaverSessionCreate, AgenticSubscriptionCancellationSaverItemCreate

class AgenticSubscriptionCancellationSaverService:
    @staticmethod
    def create_session(db: Session, data: AgenticSubscriptionCancellationSaverSessionCreate) -> AgenticSubscriptionCancellationSaverSession:
        db_obj = AgenticSubscriptionCancellationSaverSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticSubscriptionCancellationSaverSession:
        return db.query(AgenticSubscriptionCancellationSaverSession).filter(AgenticSubscriptionCancellationSaverSession.id == session_id).first()
