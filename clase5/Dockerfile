FROM ubuntu:14.04

#Instalamos firefox
RUN apt-get update && apt-get install -y firefox

#Reemplazamos 1000 con el usuario / y id del grupo
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

#Cambio de usuario
USER developer
#Variable de entorno HOME
ENV HOME /home/developer

#Comando a usar
CMD /usr/bin/firefox
