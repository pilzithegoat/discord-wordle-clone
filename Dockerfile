FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN cd google-images-dowload && python3 setup.py install
RUN mkdir dowloads
RUN apt-get update && apt-get install -y ffmpeg

CMD  ["python3", "bot.py"]