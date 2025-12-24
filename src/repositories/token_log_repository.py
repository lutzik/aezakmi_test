from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from models import TokenLog
from typing import Optional

def log_token(db: Session, user_id: str, channel: Optional[str], token_type: str, expires_in: int, ip_address: str):
    expires_at = datetime.utcnow() + timedelta(seconds=expires_in)
    log = TokenLog(
        user_id=user_id,
        channel=channel,
        token_type=token_type,
        expires_at=expires_at,
        ip_address=ip_address
    )
    db.add(log)
    db.commit()
