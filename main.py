import requests
import time


def make_request():
    response = requests.get("https://quicknotes.space/")

    print("Response status code: ", response.status_code)


SLEEP_TIME = 600

while True:
    make_request()
    time.sleep(SLEEP_TIME)
