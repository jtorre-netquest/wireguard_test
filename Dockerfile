FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    wireguard-tools \
    iproute2 \
    iptables \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY wireguard.conf /etc/wireguard/wg0.conf

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt


RUN adduser --disabled-password --gecos "" wgtest && \
    usermod -aG sudo wgtest && \
    mkdir -p /etc/sudoers.d && \
    echo "wgtest ALL=(ALL) NOPASSWD:ALL" | tee /etc/sudoers.d/wgtest && \
    chmod 0440 /etc/sudoers.d/wgtest

USER wgtest

ENTRYPOINT ["/bin/sh", "-c", "wg-quick up wg0 && exec \"$@\"", "--"]