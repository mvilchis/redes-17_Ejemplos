FROM ubuntu:latest

RUN  apt-get update && \
    apt-get install -y --no-install-recommends \
    python\
    vim \
    git\
    build-essential\
    python-qt4\
    python-pyaudio\
    python-opencv

RUN mkdir Redes-17

ADD . Redes-17

WORKDIR Redes-17

CMD ["./init.sh"]
