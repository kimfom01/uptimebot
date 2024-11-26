from celery import Celery
from dotenv import load_dotenv

import os

load_dotenv()

queue = Celery("tasks", broker=f"{os.getenv("RABBIT_MQ")}")


@queue.task
def hello(x, y):
    return x + y
