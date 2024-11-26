from datetime import datetime
from typing import Union
import uuid
from pydantic import BaseModel


class Server(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    url: str
    title: str
    interval: int
    tracking_id: Union[uuid.UUID, None] = None
    created_at: datetime = datetime.now()


class ServerCreate(BaseModel):
    url: str
    title: str
    interval: int
