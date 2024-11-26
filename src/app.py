from datetime import datetime
import uuid
from fastapi import HTTPException, status
from app import create_app
from app.tasks import hello
from app.models.server import ServerCreate, Server, db

app = create_app()


@app.get("/")
async def get_base():
    result = hello.delay(4, 4)
    print(result)
    return "Welcome to UptimeBot API"


@app.post("/track", status_code=status.HTTP_201_CREATED)
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


@app.get("/track/{tracking_id}", status_code=status.HTTP_200_OK)
async def get_track(tracking_id: uuid.UUID) -> Server:
    result = list(filter(lambda x: x.tracking_id == tracking_id, db))

    if len(result) == 0:
        raise HTTPException(status_code=404, detail="No server with that tracking link")

    return result.pop()
