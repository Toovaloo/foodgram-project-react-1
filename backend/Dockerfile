FROM python:3.8.5-slim

WORKDIR /backend
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD gunicorn backend.wsgi:application --bind 0.0.0.0:8000
