FROM python:3.13-slim

WORKDIR /bot

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE=1

ENV POETRY_VERSION=1.8.4 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update && apt-get install --no-install-recommends -y curl make \
    && curl -sSL https://install.python-poetry.org | python - \
    && apt-get clean

COPY pyproject.toml .

COPY poetry.lock .

RUN poetry install

COPY . .

USER appuser

CMD [ "poetry", "run", "python", "main.py" ]