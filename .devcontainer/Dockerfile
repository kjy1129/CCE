FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    python3 python3-pip python3-dev \
    gdb git curl wget gcc make \
    libssl-dev libffi-dev build-essential \
    tmux unzip

RUN pip3 install --upgrade pwntools
