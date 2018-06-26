FROM python:3

RUN apt-get update && apt-get install curl
RUN curl -sSL https://get.docker.com/ | sh

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./main.py" ]