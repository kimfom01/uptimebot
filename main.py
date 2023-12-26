import requests
import time


def make_request(url: str):
    response = requests.get(url=url)

    print("Response status code: ", response.status_code)


SLEEP_TIME = 600
URL = "https://quicknotes.space/"

while True:
    make_request(url=URL)
    time.sleep(SLEEP_TIME)
