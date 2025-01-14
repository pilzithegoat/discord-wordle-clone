FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV TOKEN=your_token_here

RUN mkdir dowloads
#RUN apt-get update && apt-get install -y ffmpeg

CMD  ["python3", "bot.py"]