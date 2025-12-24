from fastapi import APIRouter, Depends, Header, HTTPException, Request
from sqlalchemy.orm import Session

from database import get_db
from schemas import RtcTokenRequest, RtmTokenRequest, TokenResponse
from services.token_service import EXPIRES_IN, generate_rtc_token, generate_rtm_token

router = APIRouter(prefix="/api/tokens")

@router.post("/rtc", response_model=TokenResponse)
def get_rtc_token(token_req: RtcTokenRequest, request: Request, db: Session = Depends(get_db), x_user_id: str = Header(None)):
    if not x_user_id:
        raise HTTPException(status_code=401, detail="Missing X-User-Id header")
    try:
        token = generate_rtc_token(token_req.channel, token_req.uid, token_req.role, x_user_id, request.client.host, db)
        return {"token": token, "expires_in": EXPIRES_IN}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/rtm", response_model=TokenResponse)
def get_rtm_token(token_req: RtmTokenRequest, request: Request, db: Session = Depends(get_db), x_user_id: str = Header(None)):
    if not x_user_id:
        raise HTTPException(status_code=401, detail="Missing X-User-Id header")
    try:
        token = generate_rtm_token(token_req.uid, x_user_id, request.client.host, db)
        return {"token": token, "expires_in": EXPIRES_IN}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))