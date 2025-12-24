from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from schemas import RoomCreate, RoomResponse
from services.room_service import create_room_service

router = APIRouter(prefix="/api/rooms")

@router.post("", response_model=RoomResponse)
def create_room(room: RoomCreate, db: Session = Depends(get_db), x_user_id: str = Header(None)):
    if not x_user_id:
        raise HTTPException(status_code=401, detail="Missing X-User-Id header")
    new_room = create_room_service(db, room.name, room.is_private, room.max_participants, x_user_id)
    return {"room_id": str(new_room.id), "channel_name": new_room.agora_channel_name}