import requests
import time


def make_request():
    requests.get("https://quicknotes.space/")


SLEEP_TIME = 600

while True:
    make_request()
    time.sleep(SLEEP_TIME)
