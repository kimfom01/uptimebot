from datetime import datetime
import uuid
from fastapi import APIRouter, HTTPException, status

from app.data import db
from app.models.server import Server, ServerCreate


router = APIRouter(prefix="/tracks", tags=["tracks"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_track(server_create: ServerCreate) -> Server:
    server = Server(
        url=server_create.url,
        title=server_create.title,
        interval=server_create.interval,
    )
    tracking_id = uuid.uuid4()
    server.tracking_id = tracking_id
    server.created_at = datetime.now()
    db.append(server)

    return server


@router.get("/{tracking_id}", status_code=status.HTTP_200_OK)
async def get_track(tracking_id: uuid.UUID) -> Server:
    result = list(filter(lambda x: x.tracking_id == tracking_id, db))

    if len(result) == 0:
        raise HTTPException(status_code=404, detail="No server with that tracking link")

    return result.pop()
