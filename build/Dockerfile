FROM python:3.9-slim as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python3 -m pip install --upgrade pip

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

COPY requirements.txt requirements.txt
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM python:3.9-slim

WORKDIR /app

RUN apt-get update \
    && apt-get -y install libpq-dev gcc netcat

COPY --from=builder /app/wheels /wheels

COPY --from=builder /app/requirements.txt .

ENV PYTHONPATH="${PYTHONPATH}:/app/src"

RUN python3 -m pip install --upgrade pip

RUN pip install --no-cache /wheels/*

COPY entrypoint.sh entrypoint.sh

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]