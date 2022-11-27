FROM python:3.9.2-slim

ENV APP_HOME=/usr/src/app
RUN mkdir $APP_HOME

WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt update && apt install --no-install-recommends -y build-essential musl-dev git gcc g++ bash make python3-dev

# required to install confluent-kafka in Mac M1
RUN cd /tmp && git clone https://github.com/edenhill/librdkafka.git && \
    cd librdkafka && git checkout tags/v1.9.0 && \
    ./configure && make && make install && ldconfig && \
    cd ../ && rm -rf librdkafka

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
