FROM Ubuntu

RUN apt-get update
RUN apt install python

COPY . /OPT/CLI/
WORKDIR /OPT/CLI/

RUN pip install -r requirements.txt
ENV PYTHONPATH=/OPT/CLI/src

RUN sudo usermod -a -G video developer

