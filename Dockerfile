FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    wireguard-tools \
    iproute2 \
    iptables \
    && rm -rf /var/lib/apt/lists/*


COPY wireguard.conf /etc/wireguard/wg0.conf

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

ENTRYPOINT ["/bin/sh", "-c", "wg-quick up wg0 && exec \"$@\"", "--"]
