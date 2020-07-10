FROM ubuntu:latest

#https://hub.docker.com/repository/docker/azf0052/python-image-gallery

# Build instructions...
ENV NAME="Test"
ENV PG_HOST=image-gallery
ENV PG_PORT=5432
ENV IG_DATABASE=image-gallery
ENV IG_USER=image_gallery
ENV IG_PASSWD=test
ENV IG_PASSWD_FILE=
ENV S3_IMAGE_BUCKET=edu.au.cc.imagegallery


RUN apt-get update -y && apt-get install python3 -y  
RUN apt-get install -y git
RUN git clone https://github.com/adam190/python-image-gallery2.git
RUN useradd -m test

COPY python-image-gallery2/build/libs/python-image-gallery2.jar /python-image-gallery2/
WORKDIR /python-image-gallery2

USER test


# Boot command
CMD ["python", "-jar", "python-image-gallery2-all.jar"]

