FROM ubuntu:latest

#https://hub.docker.com/repository/docker/azf0052/python-image-gallery

# Build instructions...
ENV PG_HOST=image-gallery
ENV PG_PORT=5432
ENV IG_DATABASE=image-gallery
ENV IG_PASSWD=test

RUN apt-get update -y && apt-get install python3 -y
COPY app /app/  
RUN apt-get install -y git
RUN git clone https://github.com/adam190/python-image-gallery2.git
RUN useradd -m test

#COPY python-image-gallery2/build/libs/python-image-gallery2 /python-image-gallery2/
WORKDIR /python-image-gallery2/docker

USER test


# Boot command
CMD ["/usr/bin/python3", "/app/hello.py"]

