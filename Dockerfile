FROM python:3.7

ENV LISTEN_PORT=5000
EXPOSE 5000

RUN mkdir usr/app
WORKDIR usr/app

COPY . .

RUN pip install -r requirements.txt

CMD python app_1.py
