import uuid
from sqlalchemy.orm import Session

from models import Room

def create_room(db: Session, name: str, is_private: bool, max_participants: int, created_by: str):
    channel_name = f"channel_{uuid.uuid4().hex[:10]}"
    room = Room(
        name=name,
        agora_channel_name=channel_name,
        is_private=is_private,
        max_participants=max_participants,
        created_by=created_by
    )
    db.add(room)
    db.commit()
    db.refresh(room)
    return room
