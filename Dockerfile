FROM python:3.10-slim-buster

RUN python -m pip install --upgrade pip

WORKDIR  /app

COPY ../requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY ../. .

CMD uvicorn run:app --host 0.0.0.0 --port 8000 --reload
