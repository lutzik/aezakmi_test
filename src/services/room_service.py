from sqlalchemy.orm import Session

from repositories.room_repository import create_room

def create_room_service(db: Session, name: str, is_private: bool, max_participants: int, user_id: str):
    return create_room(db, name, is_private, max_participants, user_id)
