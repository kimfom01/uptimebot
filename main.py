import os
import requests
import time
from dotenv import load_dotenv


load_dotenv()

config = {"URL": os.getenv("URL"), "SLEEP_TIME": int(os.getenv("SLEEP_TIME"))}


def make_request(url: str):
    response = requests.get(url=url)

    print(
        "Response status code: ",
        response.status_code,
        "=> message: ",
        response.text,
    )


try:
    while True:
        make_request(url=config["URL"])
        time.sleep(int(config["SLEEP_TIME"]))
except Exception as ex:
    print(str(ex))
