import os
from dotenv import load_dotenv

load_dotenv()

AGORA_APP_ID = os.getenv("AGORA_APP_ID")
AGORA_APP_CERTIFICATE = os.getenv("AGORA_APP_CERTIFICATE")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")
