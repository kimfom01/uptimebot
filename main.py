import requests
import time


def make_request(url: str):
    response = requests.get(url=url)

    print(
        "Response status code: ",
        response.status_code,
        "=> message: ",
        response.text,
    )


SLEEP_TIME = 180
URL = "https://emailpostapi.onrender.com/health"

while True:
    make_request(url=URL)
    time.sleep(SLEEP_TIME)
