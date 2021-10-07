FROM ubuntu

RUN apt-get update
RUN apt install -y python \
    &&  apt install -y python3-pip \
    && apt-get install -y  libgl1 

COPY . /OPT/CLI/
WORKDIR /OPT/CLI/

ENV PYTHONPATH=/OPT/CLI/src

RUN  pip3 install -r requirements \
    &&  apt -y install lolcat




