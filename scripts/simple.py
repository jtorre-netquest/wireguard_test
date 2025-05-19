import requests
import os
import sys

def get_ssl_info(url, proxy):
    try:
        proxies = {
            "http": proxy,
            "https": proxy
        }
        response = requests.get(url, proxies=proxies, stream=True)

        print(response.status_code)
        cert = response.raw.connection.sock.getpeercert()
        issuer = dict(x[0] for x in cert.get("issuer", []))
        subject_alt_names = cert.get("subjectAltName", [])

        print("Issuer:", issuer, flush=True)
        print("Subject Alternative Names:", subject_alt_names, flush=True)
    except Exception as e:
        print(f"Error: {e}", flush=True)

if len(sys.argv) != 2:
    print("Use: python simple.py <proxy_host:port>", flush=True)
    sys.exit(1)

proxy = sys.argv[1]
proxy = "http://" + proxy

# url = "https://example.com/"
url = "https://4411.flitsmeister.app/nl/zones"
print("---------- PROXY ----------", flush=True)
get_ssl_info(url, proxy)

