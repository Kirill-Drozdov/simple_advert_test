FROM python:3.10-slim-buster

RUN python -m pip install --upgrade pip

WORKDIR  /app

COPY ../requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY ../. .

# RUN alembic upgrade head

CMD uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
