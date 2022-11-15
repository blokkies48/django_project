# Massive help from this video https://www.youtube.com/watch?v=W5Ov0H7E_o4

# docker machine used linux
FROM python:3.10-slim-buster

# the dir the docker is running from
WORKDIR /app

# Copies the req file as req
COPY requirements.txt requierements.txt

# installs requirements
RUN pip install -r requierements.txt

# Copies all files from current dir to work dir
COPY . .

# Command that is ran
CMD [ "python","manage.py","runserver", "0.0.0.0:8000" ]
