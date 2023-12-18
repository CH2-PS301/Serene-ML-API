FROM python:3.10.3-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /workspace

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install -r requirements.txt

CMD uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
