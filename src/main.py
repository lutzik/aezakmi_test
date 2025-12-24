import logging
import os

from fastapi import FastAPI
from fastapi import status
from fastapi.responses import JSONResponse

from database import Base, engine
from routers import auth, rooms, tokens

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

logging.basicConfig(level=logging.INFO)

app = FastAPI()

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(auth.router)
app.include_router(tokens.router)
app.include_router(rooms.router)

for route in tokens.router.routes:
	route.endpoint = limiter.limit("10/minute")(route.endpoint)

Base.metadata.create_all(bind=engine)

@app.get("/health")
async def health_check():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "healthy"})