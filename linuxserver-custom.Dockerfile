# FROM debian:bullseye-slim
FROM lscr.io/linuxserver/wireguard:latest

RUN apk update && apk add \
    sudo \
    python3 \
    py3-pip \
    py3-requests