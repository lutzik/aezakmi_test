from fastapi import APIRouter, Header, HTTPException

from schemas import AuthResponse

router = APIRouter(prefix="/api/auth")

@router.post("/simple", response_model=AuthResponse)
def simple_auth(x_user_id: str = Header(None)):
    if not x_user_id:
        raise HTTPException(status_code=401, detail="Missing X-User-Id header")
    return {"message": "Authenticated"}