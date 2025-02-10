# FROM debian:bullseye-slim
FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    bc \
    curl \
    grep \
    iproute2 \
    iptables \
    iputils-ping \
    kmod \
    libcap2-bin \
    qrencode \
    net-tools \
    openresolv \
    wireguard-tools \
    sudo \
    procps \
    traceroute \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN sed -i 's|\[\[ $proto == -4 \]\] && cmd sysctl -q net\.ipv4\.conf\.all\.src_valid_mark=1|[[ $proto == -4 ]] \&\& [[ $(sysctl -n net.ipv4.conf.all.src_valid_mark) != 1 ]] \&\& cmd sysctl -q net.ipv4.conf.all.src_valid_mark=1|' /usr/bin/wg-quick

RUN echo "wireguard" >> /etc/modules && \
cd /usr/sbin && \
for i in ! !-save !-restore; do \
  rm -rf iptables$(echo "${i}" | cut -c2-) && \
  rm -rf ip6tables$(echo "${i}" | cut -c2-) && \
  ln -s iptables-legacy$(echo "${i}" | cut -c2-) iptables$(echo "${i}" | cut -c2-) && \
  ln -s ip6tables-legacy$(echo "${i}" | cut -c2-) ip6tables$(echo "${i}" | cut -c2-); \
done

COPY wireguard.conf /etc/wireguard/wg0.conf

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt


RUN adduser --disabled-password --gecos "" wgtest && \
    usermod -aG sudo wgtest && \
    mkdir -p /etc/sudoers.d && \
    echo "wgtest ALL=(ALL) NOPASSWD:ALL" | tee /etc/sudoers.d/wgtest && \
    chmod 0440 /etc/sudoers.d/wgtest

USER wgtest

ENTRYPOINT ["/bin/sh", "-c", "sudo wg-quick up wg0 && exec \"$@\"", "--"]