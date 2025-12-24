import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy import String
import uuid

from database import Base

class Room(Base):
    __tablename__ = "rooms"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    agora_channel_name = Column(String, unique=True, nullable=False)
    is_private = Column(Boolean, default=False)
    max_participants = Column(Integer, nullable=False)
    created_by = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class TokenLog(Base):
    __tablename__ = "tokens_log"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    channel = Column(String)
    token_type = Column(String, nullable=False)  # 'rtc' or 'rtm'
    issued_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)
    ip_address = Column(String, nullable=False)