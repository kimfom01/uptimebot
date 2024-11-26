from app import create_app
from app.tasks import hello
from .routers import track


app = create_app()
app.include_router(track.router)


@app.get("/")
async def get_base():
    result = hello.delay(4, 4)
    print(result)
    return "Welcome to UptimeBot API"
