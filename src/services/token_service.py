import logging
from datetime import timedelta, datetime

from sqlalchemy.orm import Session

from config import AGORA_APP_ID, AGORA_APP_CERTIFICATE
from repositories.token_log_repository import log_token
from agora_token_builder import RtcTokenBuilder, RtmTokenBuilder

logger = logging.getLogger(__name__)

EXPIRES_IN = 3600

Role_Publisher = 1
Role_Subscriber = 2

def generate_rtc_token(channel: str, uid: str, role: str, user_id: str, ip_address: str, db: Session):
    if not AGORA_APP_ID or not AGORA_APP_CERTIFICATE:
        raise ValueError("Agora credentials not set")

    if role not in ["host", "audience"]:
        raise ValueError("Invalid role")

    agora_role = Role_Publisher if role == "host" else Role_Subscriber

    token = RtcTokenBuilder.buildTokenWithAccount(
        AGORA_APP_ID, AGORA_APP_CERTIFICATE, channel, uid, agora_role, EXPIRES_IN
    )

    log_token(db, user_id, channel, "rtc", EXPIRES_IN, ip_address)
    logger.info(f"RTC token generated for user {user_id} in channel {channel}")
    return token

def generate_rtm_token(uid: str, user_id: str, ip_address: str, db: Session):
    if not AGORA_APP_ID or not AGORA_APP_CERTIFICATE:
        raise ValueError("Agora credentials not set")

    expiration_time_in_seconds = EXPIRES_IN
    privilege_expired_ts = int(datetime.utcnow().timestamp()) + expiration_time_in_seconds

    token = RtmTokenBuilder.buildToken(
        AGORA_APP_ID,
        AGORA_APP_CERTIFICATE,
        uid,
        expiration_time_in_seconds,
        privilege_expired_ts
    )

    log_token(db, user_id, None, "rtm", EXPIRES_IN, ip_address)
    logger.info(f"RTM token generated for user {user_id}")
    return token