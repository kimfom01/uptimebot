FROM python:3.10-slim

ADD . .

RUN pip install -r ./requirements.txt

CMD [ "python", "-u", "main.py" ]