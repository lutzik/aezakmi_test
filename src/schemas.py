from pydantic import BaseModel

class AuthResponse(BaseModel):
    message: str

class RtcTokenRequest(BaseModel):
    channel: str
    uid: str
    role: str

class RtmTokenRequest(BaseModel):
    uid: str

class TokenResponse(BaseModel):
    token: str
    expires_in: int

class RoomCreate(BaseModel):
    name: str
    is_private: bool
    max_participants: int

class RoomResponse(BaseModel):
    room_id: str
    channel_name: str