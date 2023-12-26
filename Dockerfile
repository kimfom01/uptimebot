FROM python:3.10-slim

WORKDIR /bot

ADD . .

RUN pip install -r ./requirements.txt

CMD [ "python", "-u", "main.py" ]