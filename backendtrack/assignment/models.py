from db_config import Base  # CRITICAL: Inherit from the shared Base instance!
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime, timezone

class Task(Base):
    __tablename__ = "task_table"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    done = Column(Boolean, default=False, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
