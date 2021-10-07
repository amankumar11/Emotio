FROM ubuntu

RUN apt-get update
RUN apt install -y python\
    &&  apt install -y python3-pip \
    && apt-get install ffmpeg libsm6 libxext6  -y

COPY . /OPT/CLI/
WORKDIR /OPT/CLI/

ENV PYTHONPATH=/OPT/CLI/src

RUN  pip3 install -r requirements \
    &&  apt -y install lolcat




