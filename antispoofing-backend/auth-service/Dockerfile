FROM python:3.9.2-slim

ENV APP_HOME=/usr/src/app
RUN mkdir $APP_HOME

WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt update && apt install --no-install-recommends -y --fix-missing build-essential \
    musl-dev \
    gcc \
    g++ \
    bash \
    make \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    libgtk2.0-dev \
    pkg-config \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

# required to install confluent-kafka in Mac M1
RUN cd /tmp && git clone https://github.com/edenhill/librdkafka.git && \
    cd librdkafka && git checkout tags/v1.9.0 && \
    ./configure && make && make install && ldconfig && \
    cd ../ && rm -rf librdkafka

RUN cd ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python3 setup.py install --yes USE_AVX_INSTRUCTIONS

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
