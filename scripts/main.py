import requests
import os
import sys

def get_ssl_info(url, proxy=None):
    try:
        if proxy:
            proxies = {
                "http": proxy,
                "https": proxy
            }
            response = requests.get(url, proxies=proxies, stream=True)
        else:
            response = requests.get(url, stream=True)

        print(response.status_code)
        cert = response.raw.connection.sock.getpeercert()
        issuer = dict(x[0] for x in cert.get("issuer", []))
        subject_alt_names = cert.get("subjectAltName", [])

        print("Issuer:", issuer)
        print("Subject Alternative Names:", subject_alt_names)
    except Exception as e:
        print(f"Error: {e}")


if len(sys.argv) != 2:
    print("Use: python main.py <proxy_host:port>")
    sys.exit(1)

proxy = sys.argv[1]

proxy = "http://" + proxy

url = "https://example.com/"

print("--------- CON PROXY ----------")
get_ssl_info(url, proxy)

print("\n--------- SIN PROXY ----------")
get_ssl_info(url)
