FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install sudo
RUN sudo apt upgrade -y
RUN sudo apt update -y
RUN sudo apt-get install -y \
    python3.7 \
    python3.7-venv \
    python3.7-dev  \
    python3-pip
RUN sudo ln -s /usr/bin/python3.7 /usr/bin/python
RUN apt-get -y install libgl1-mesa-glx

WORKDIR /app
