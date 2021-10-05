FROM Ubuntu

RUN apt-get update
RUN apt install python

COPY . /OPT/CLI/
WORKDIR /OPT/CLI/

ENV PYTHONPATH=/OPT/CLI/src
RUN pip install -r requirements.txt

RUN sudo usermod -a -G video developer

