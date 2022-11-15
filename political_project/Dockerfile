# Massive help from this video https://www.youtube.com/watch?v=W5Ov0H7E_o4

FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requierements.txt

RUN pip install -r requierements.txt

COPY . .

CMD [ "python","manage.py","runserver", "0.0.0.0:8000" ]