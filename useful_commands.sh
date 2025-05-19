docker network create \
  --subnet=192.168.100.0/24 \
  wireguard-net

docker run -d \
  --name=wg-server \
  --cap-add=NET_ADMIN \
  --cap-add=SYS_MODULE \
  --network=wireguard-net \
  --ip=192.168.100.2 \
  -e PUID=1000 \
  -e PGID=1000 \
  -e SERVERPORT=51820 \
  -e PEERS=1 \
  -e ALLOWEDIPS=0.0.0.0/0 \
  -v wg-server-config:/config \
  --sysctl="net.ipv4.conf.all.src_valid_mark=1" \
  -p 51820:51820/udp \
  lscr.io/linuxserver/wireguard:latest

docker exec wg-server cat /config/peer1/peer1.conf

docker run -d \
  --name=wg-client \
  --cap-add=NET_ADMIN \
  --network=wireguard-net \
  -v $(pwd)/wireguard_confs/client.conf:/config/wg_confs/wg0.conf \
  --sysctl="net.ipv4.conf.all.src_valid_mark=1" \
  lscr.io/linuxserver/wireguard:latest

docker container stop wg-client && docker container rm wg-client

docker run -d \
  --name=wg-client \
  --cap-add=NET_ADMIN \
  --network=wireguard-net \
  -v $(pwd)/wg.conf:/config/wg_confs/wg0.conf \
  --sysctl="net.ipv4.conf.all.src_valid_mark=1" \
  test-wireguard:latest

docker run --name=wg-client \
    --cap-add=NET_ADMIN \
    --network=wireguard-net \
    -v $(pwd)/main.py:/app/main.py \
    -v $(pwd)/wg.conf:/etc/wireguard/wg0.conf \
    --sysctl="net.ipv4.conf.all.src_valid_mark=1" \
    test-wireguard:custom python /app/main.py